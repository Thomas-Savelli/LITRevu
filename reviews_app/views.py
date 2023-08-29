from itertools import chain
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from . import models, forms
# Create your views here.


@login_required
def home(request):
    critiques = models.Critique.objects.filter(
        Q(contributors__in=request.user.follows.all()) | Q(note=True))
    tickets = models.Ticket.objects.filter(
        uploader__in=request.user.follows.all()).exclude(critique__in=critiques)
    critiques_and_tickets = sorted(chain(critiques, tickets), key=lambda instance: instance.time_created, reverse=True)
    return render(request, 'reviews_app/home.html', context={'critiques_and_tickets': critiques_and_tickets})


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


@login_required
def edit_critique(request, critique_id):
    critique = get_object_or_404(models.Critique, id=critique_id)
    edit_form = forms.CritiqueForm(instance=critique)
    delete_form = forms.DeleteCritiqueForm()
    if request.method == 'POST':
        if 'edit_critique' in request.POST:
            edit_form = forms.CritiqueForm(request.POST, instance=critique)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
            if 'delete_critique' in request.POST:
                delete_form = forms.DeleteCritiqueForm(request.POST)
                if delete_form.is_valid():
                    critique.delete()
                    return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form}
    return render(request, 'reviews_app/edit_critique.html', context=context)


@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'reviews_app/follow_users_form.html', context={'form': form})
