from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Article

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateArticleForm(Article):
    class Mete:
        model= Article
        fields = ['id','pavadinimas', 'autorius', 'pareigos', 'straipsnis', 'pub_dt', 'edit_dt', 'kategorija','foto']
