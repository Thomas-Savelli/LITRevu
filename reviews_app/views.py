from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms, models

# Create your views here.


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'reviews_app/home.html', context={'tickets': tickets})


@login_required
def ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'reviews_app/ticket.html', context={'form': form})
