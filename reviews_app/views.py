from itertools import chain
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q

from . import models, forms
from .forms import SearchUsersForm
from authentication.models import User


@login_required
def home(request):
    user = request.user
    # Récupérez les tickets associés à l'utilisateur connecté
    user_tickets = models.Ticket.objects.filter(uploader=user)

    # Récupérez les critiques de l'utilisateur connecté
    user_critiques = models.Critique.objects.filter(author=user)

    # Récupérez les tickets et critiques associés aux utilisateurs suivis
    tickets = models.Ticket.objects.filter(uploader__in=request.user.follows.all())

    # Récupérez les critiques associées aux utilisateurs suivis
    critiques = models.Critique.objects.filter(
        Q(contributors__in=request.user.follows.all()) | Q(ticket__in=tickets)).exclude(author=user)

    # Créez une liste pour stocker les IDs des tickets pour lesquels l'utilisateur a créé une critique
    user_has_created_critique = []

    # Parcours les tickets pour vérifier si l'utilisateur a créé une critique
    for ticket in tickets:
        if models.Critique.objects.filter(ticket=ticket, author=user).exists():
            # Si l'utilisateur a créé une critique pour ce ticket, ajouter son ID à la liste
            user_has_created_critique.append(ticket.id)

    # Combinez les tickets et critiques de l'utilisateur connecté, ainsi que ceux des utilisateurs suivis,
    critiques_and_tickets = sorted(
        chain(user_tickets, critiques, tickets, user_critiques),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    print(critiques_and_tickets)
    context = {
        'critiques_and_tickets': critiques_and_tickets,
        'user_has_created_critique': user_has_created_critique,
    }
    return render(request, 'reviews_app/home.html', context=context)


@login_required
def ticket_create(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'reviews_app/ticket_create.html', context={'ticket_form': ticket_form})


@login_required
def create_critique_from_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    critique_form = forms.CritiqueForm()

    if request.method == 'POST':
        critique_form = forms.CritiqueForm(request.POST)
        if critique_form.is_valid():
            critique = critique_form.save(commit=False)
            critique.author = request.user
            critique.ticket = ticket
            critique.save()
            critique.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
            return redirect('home')

    context = {
        'critique_form': critique_form,
        'ticket': ticket,
    }
    return render(request, 'reviews_app/create_critique_from_ticket.html', context=context)


@login_required
def critique_and_ticket_create(request):
    critique_form = forms.CritiqueForm()
    ticket_form = forms.TicketForm()

    if request.method == 'POST':
        critique_form = forms.CritiqueForm(request.POST)
        ticket_form = forms.TicketForm(request.POST, request.FILES)

        if all([critique_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            critique = critique_form.save(commit=False)
            critique.author = request.user
            critique.save()
            critique.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
        return redirect('home')

    context = {
        'critique_form': critique_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'reviews_app/create_critique_post.html', context=context)


# Vue pour éditer un ticket
@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.user != ticket.uploader:
        return redirect('user_posts')

    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('user_posts')
    else:
        form = forms.TicketForm(instance=ticket)

    context = {
        'form': form,
    }
    return render(request, 'reviews_app/edit_ticket.html', context)


# Vue pour supprimer un ticket
@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.user == ticket.uploader:
        if request.method == 'POST':
            ticket.delete()
            return redirect('user_posts')
        return render(request, 'reviews_app/ticket_delete.html')
    else:
        return redirect('user_posts')


# Vue pour éditer une critique
@login_required
def edit_critique(request, critique_id):
    critique = get_object_or_404(models.Critique, id=critique_id)
    if request.user != critique.author:
        return redirect('user_posts')

    if request.method == 'POST':
        form = forms.CritiqueForm(request.POST, instance=critique)
        if form.is_valid():
            form.save()
            return redirect('user_posts')
    else:
        form = forms.CritiqueForm(instance=critique)

    context = {
        'form': form,
    }
    return render(request, 'reviews_app/edit_critique.html', context)


@login_required
def delete_critique(request, critique_id):
    critique = get_object_or_404(models.Critique, id=critique_id)
    if request.user == critique.author:
        if request.method == 'POST':
            critique.delete()
            return redirect('user_posts')
        return render(request, 'reviews_app/critique_delete.html')
    else:
        return redirect('user_posts')


@login_required
def user_posts(request):
    user = request.user
    user_tickets = models.Ticket.objects.filter(uploader=user)
    user_critiques = models.Critique.objects.filter(author=user)

    # Créez une liste pour stocker les IDs des tickets pour lesquels l'utilisateur a créé une critique
    tickets_with_critique = []

    # Parcourez les tickets pour vérifier si l'utilisateur a créé une critique pour chaque ticket
    for ticket in user_tickets:
        if models.Critique.objects.filter(ticket=ticket, author=user).exists():
            # Si l'utilisateur a créé une critique pour ce ticket, ajoutez son ID à la liste
            tickets_with_critique.append(ticket.id)

    # Créez une liste qui combine les critiques et les tickets de l'utilisateur
    critiques_and_tickets = sorted(chain(user_critiques, user_tickets),
                                   key=lambda instance: instance.time_created, reverse=True)

    context = {
        'critiques_and_tickets': critiques_and_tickets,
        'tickets_with_critique': tickets_with_critique,
    }

    return render(request, 'reviews_app/user_posts.html', context=context)


@login_required
def follow_users(request):
    search_results = []

    if request.method == 'POST':
        search_user = request.POST.get('search_user', '').strip()
        if search_user:
            search_results = User.objects.filter(username__icontains=search_user).exclude(id=request.user.id)

        else:
            user_id = request.POST.get('user_id')
            if user_id:
                user_to_follow = get_object_or_404(User, id=user_id)
                request.user.follows.add(user_to_follow)

    return render(request, 'reviews_app/follow_users_form.html', {'search_results': search_results})


@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    if request.user in user_to_unfollow.followed_by.all():
        request.user.follows.remove(user_to_unfollow)
    return redirect('follow_users')


@login_required
def search_users(request):
    if request.method == 'POST':
        search_form = forms.SearchUsersForm(request.POST)
        if search_form.is_valid():
            query = search_form.cleaned_data['search_user']
            users = User.objects.filter(username__icontains=query)
            users_list = [{'username': user.username} for user in users]
            return JsonResponse({'users': users_list})
    else:
        search_form = SearchUsersForm()
    return render(request, 'reviews_app/follow_users_form.html', {'search_form': search_form})
