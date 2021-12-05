from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=40,blank=True)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    github = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.username

class post(models.Model):
    title = models.CharField(max_length=40, blank=True)
    body = models.TextField(max_length=900, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    author = models.ForeignKey(user, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.author.username




    