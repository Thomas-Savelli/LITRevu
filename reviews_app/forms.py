from django import forms

from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'image', 'description']


class CritiqueForm(forms.ModelForm):
    edit_critique = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Critique
        fields = ['commentaire', 'note', 'body']


class DeleteCritiqueForm(forms.Form):
    delete_critique = forms.BooleanField(widget=forms.HiddenInput, initial=True)
