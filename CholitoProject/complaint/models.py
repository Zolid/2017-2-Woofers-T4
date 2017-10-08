from django.db import models



class Complaint(models.Model):
	COMPLAINT_OPTIONS = (
	(1, "Maltrato"),
	)

	description = models.TextField(max_length=1000)
	case = models.SmallIntegerField(choices = COMPLAINT_OPTIONS)



class ComplaintImages(models.Model):
	image = models.ImageField(upload_to='complaints/')
	complaint = models.ForeignKey('Complaint',on_delete=models.CASCADE)


