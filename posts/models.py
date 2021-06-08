from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profiles


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    liked = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
