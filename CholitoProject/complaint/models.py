from django.db import models


class Complaint(models.Model):
    COMPLAINT_OPTIONS = (
        (1, "Maltrato"),
    )

    description = models.TextField(max_length=1000)
    case = models.SmallIntegerField(choices=COMPLAINT_OPTIONS)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    directions = models.TextField(max_length=200, null=True)


class ComplaintImages(models.Model):
    image = models.ImageField(upload_to='complaints/')
    complaint = models.ForeignKey('Complaint', on_delete=models.CASCADE)
