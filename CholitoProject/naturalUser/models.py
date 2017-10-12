from django.db import models
from django.shortcuts import redirect
from django.contrib.auth.models import User


class NaturalUser(models.Model):
    user = models.OneToOneField(User)

    def get_index(self):
        return redirect('user-index')
