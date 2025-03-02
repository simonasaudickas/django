from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Straipsnis

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Straipsnis
        fields = '__all__'
        """fields = ['pavadinimas', 'autorius', 'pareigos', 'straipsnis', 'pub_dt', 'edit_dt', 'kategorija','foto']"""
        exclude = ['auto_increment_id',]
