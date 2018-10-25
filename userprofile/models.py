from django.db import models
from datetime import datetime


# Create your models here.

class UserAccount(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    dob = models.DateTimeField(default=datetime.now, blank=True)
    file = models.FileField(upload_to="userprofile/static/userprofile/files", blank=True)
    image = models.ImageField(upload_to="userprofile/static/userprofile/img/")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
