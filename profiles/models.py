from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default='avatar.png', upload_to='avatars')
    updated = models.DateTimeField(auto_now=True)
    crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of the user {self.user.username}"
