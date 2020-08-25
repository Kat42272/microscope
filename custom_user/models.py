from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Study Hall Group assistance with this section
# Information from https://docs.djangoproject.com/en/3.1/topics/auth/customizing/
# William Vincent Django For Beginners Chapter 8
# Peter Marsh helped me undo a lot of confusion from William Vincent's setup
# Matt Perry assisted me to debug and issue

class CustomUser(AbstractUser):
  age = models.PositiveIntegerField(null=True, blank=True)
  display_name = models.CharField(null=True, blank=True, max_length=150)
