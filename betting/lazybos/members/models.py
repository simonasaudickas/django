from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
class Autorius(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    def __str__(self):
        return self.User.username

class Kategorija(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# Create your models here.
class Straipsnis(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    pavadinimas = models.CharField(max_length=100)
    autorius = models.ForeignKey(Autorius, on_delete=models.CASCADE)
    pareigos = models.CharField(max_length=50)
    overview = models.TextField()
    straipsnis = models.TextField()
    pub_dt = models.DateTimeField(auto_now=True)
    edit_dt = models.DateTimeField(auto_now=False)
    kategorija = models.ManyToManyField(Kategorija)
    foto = models.ImageField(upload_to='static/images/')
    def __str__(self):
        return self.pavadinimas