from django.db import models
from django.contrib.auth.models import User

class usersprofile(models.Model):
  user = models.OneToOneField(User, related_name='users', on_delete=models.CASCADE)