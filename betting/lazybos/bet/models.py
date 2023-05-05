from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False, blank=False)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    pub_dt = models.DateTimeField(auto_now=False)
    def __str__(self):
        return self.name

class Bet(models.Model):
    bet_object= models.CharField(max_length=250)
    bet_desc = models.TextField()
    def __str__(self):
        return self.bet_object

class Options(models.Model):
    choice = models.CharField(max_length=100)
    parent = models.ForeignKey("Bet",on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.choice