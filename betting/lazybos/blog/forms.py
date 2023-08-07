from django import forms
from .models import Post, Comment
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    foto = forms.ImageField(label='Pridėti paveikslėlį', required=False)
    class Meta:
        model = Post
        fields = ['pavadinimas', 'turinys','foto']
        widgets = {
            'pavadinimas': forms.TextInput(attrs={'class': 'form-control'}),
            'turinys': TinyMCE(attrs={'cols': 80, 'rows': 30}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
