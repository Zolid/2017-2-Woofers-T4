from django.contrib.auth.models import User
from django.db import models

UserTypes = (
    (0, 'admin'),
    (1, 'natural')
)


class AnUser(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=200)
    user_type = models.IntegerField(default=1, choices=UserTypes)
