from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField(max_length= 100000)
    name = models.CharField(max_length = 100, null=True, blank=True)
    photo = models.ImageField(upload_to='photoes/', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'