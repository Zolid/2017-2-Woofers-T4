from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect


class NaturalUser(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='n_users/avatar/')

    def save(self, *args, **kwargs):
        super(NaturalUser, self).save(*args, **kwargs)
        self.user.email = self.user.username
        self.user.save()

    def __str__(self):
        return "Natural user " + self.user.username

    def get_index(self):
        return redirect('user-index')
