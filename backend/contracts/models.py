from django.db import models

class FileUpload(models.Model):
	File = models.FileField(upload_to='excel/')
	addition_date = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)