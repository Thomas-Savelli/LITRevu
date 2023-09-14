from django.contrib.auth import get_user_model
from django import forms

from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class CritiqueForm(forms.ModelForm):
    edit_critique = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    # Définissez les choix de note directement dans le formulaire
    note = forms.ChoiceField(
        label='Note',
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'note-buttons'}),)

    class Meta:
        model = models.Critique
        fields = ['commentaire', 'note', 'body']


class DeleteCritiqueForm(forms.Form):
    delete_critique = forms.BooleanField(widget=forms.HiddenInput, initial=True)


User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    search_user = forms.CharField(label='Recherher un utilisateur', max_length=100, required=False)

    class Meta:
        model = User
        fields = ['follows']


class SearchUsersForm(forms.Form):
    search_user = forms.CharField(label='Rechercher un utilisateur', max_length=100,
                                  widget=forms.TextInput(attrs={'id': 'search-user'}))
