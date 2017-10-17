from django.db import models

from complaint.models import Complaint, AnimalType


class AnimalImage(models.Model):
    image = models.ImageField(upload_to='animals/')
    complaint = models.ForeignKey('Animal', on_delete=models.CASCADE)


class Animal(models.Model):
    GENDER_OPTIONS = (
        (1, "Male"),
        (2, "Female"),
    )

    name = models.TextField(max_length=100)
    from_complaint = models.ForeignKey(Complaint, null=True)
    gender = models.SmallIntegerField(choices=GENDER_OPTIONS)
    description = models.TextField(max_length=1000)
    animal_type = models.ForeignKey(AnimalType)
    color = models.TextField(max_length=50)
    estimated_age = models.PositiveSmallIntegerField()
    days_in_adoption = models.IntegerField()
