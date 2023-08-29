from django.contrib.auth import get_user_model
from django import forms

from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class CritiqueForm(forms.ModelForm):
    edit_critique = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Critique
        fields = ['commentaire', 'note', 'body']


class DeleteCritiqueForm(forms.Form):
    delete_critique = forms.BooleanField(widget=forms.HiddenInput, initial=True)


User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
