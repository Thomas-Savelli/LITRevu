from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from . import models, forms
# Create your views here.


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    critiques = models.Critique.objects.all()
    return render(request, 'reviews_app/home.html', context={'tickets': tickets, 'critiques': critiques})


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
            critique.user = request.user
            critique.save()
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
        'delete_form': delete_form
    }
    return render(request, 'reviews_app/edit_critique.html', context=context)
