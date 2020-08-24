from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Study Hall Group assistance with this section
# Used information from https://docs.djangoproject.com/en/3.1/topics/auth/customizing/
# William Vincent Django For Beginners Chapter 8

class CustomUser(AbstractUser):
  age = models.PositiveIntegerField(null=True, blank=True)