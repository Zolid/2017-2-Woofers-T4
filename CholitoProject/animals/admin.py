from django.contrib import admin
from animals import models

# Register your models here.
admin.site.register(models.AnimalImage)
admin.site.register(models.Animal)
