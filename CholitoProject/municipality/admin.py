from django.contrib import admin
from municipality.models import Municipality, MunicipalityUser
# Register your models here.


class MunicipalityAdmin(admin.ModelAdmin):
    fields = ('password', 'first_name', 'last_name', 'username',)


admin.site.register(Municipality)
admin.site.register(MunicipalityUser, MunicipalityAdmin)
