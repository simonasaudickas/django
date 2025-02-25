from django.forms import ModelForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,label='Vardas, Pavardė')
    email = forms.EmailField(validators=[EmailValidator()],label='El.paštas')
    phone = forms.CharField(max_length=15, label='Telefonas')
    subject = forms.CharField(max_length=100, label='Žinutės pavadinimas')
    message = forms.CharField(widget=forms.Textarea, label='Užklausos tekstas')