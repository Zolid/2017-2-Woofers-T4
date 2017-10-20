from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect


class NaturalUser(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return "Natural user " + self.user.username

    def get_index(self):
        return redirect('user-index')
