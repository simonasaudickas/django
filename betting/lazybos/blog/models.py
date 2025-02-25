from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Kategorija(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Post(models.Model):
    pavadinimas = models.CharField(max_length=255)
    turinys = HTMLField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')
    kategorija = models.ManyToManyField(Kategorija)
    foto = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.pavadinimas


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.pavadinimas}'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


