from django.contrib import admin
from ong.models import ONG, ONGUser

# Register your models here.
class ONGAdmin(admin.ModelAdmin):
    fields = ('password', 'first_name', 'last_name', 'username',)

admin.site.register(ONG)
admin.site.register(ONGUser,ONGAdmin)
