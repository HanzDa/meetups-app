from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Sign up with your email')
    