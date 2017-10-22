from django.contrib.auth.models import User, Permission
from django.db import models
from django.shortcuts import render, redirect

from complaint.models import AnimalType


class NaturalUser(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='n_users/avatar/')

    def save(self, *args, **kwargs):
        super(NaturalUser, self).save(*args, **kwargs)
        if not self.user.has_perm('natural_user_access'):
            permission = Permission.objects.get(codename='natural_user_access')
            self.user.user_permissions.add(permission)
        self.user.save()

    def __str__(self):
        return "Natural user " + self.user.username

    def get_index(self, request, context=None):
        if context:
            return render(request, 'index.html', context)
        user = NaturalUser.objects.get(user=request.user)
        return redirect('user-index')
