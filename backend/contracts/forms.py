from django import forms
from .models import FileUpload


class FileUploadForm(forms.ModelForm):
	File = forms.FileField()

	class Meta:
	    model = FileUpload
	    fields = ['File',]
