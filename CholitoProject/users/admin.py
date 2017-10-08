from django.contrib import admin
from users.models import NaturalUser

# Register your models here.
class NaturaUsersAdmin(admin.ModelAdmin):
    fields = ('password', 'first_name', 'last_name', 'username',)

admin.site.register(NaturalUser,NaturaUsersAdmin)
