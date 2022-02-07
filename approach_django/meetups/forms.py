from django import forms

from .models import Participant

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        # define which fields should be populated in the form
        fields = ['email']