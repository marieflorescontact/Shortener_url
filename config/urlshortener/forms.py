'''
Shortener Forms urlshortener/forms.py
'''

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Shortener


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))
    wished_url = forms.CharField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Choose your short url"}))

    class Meta:
        model = Shortener
        fields = ('long_url',)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'email', 'password1', 'password2']
