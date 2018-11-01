from django.http import HttpResponse
from django.shortcuts import render
from .forms import FileUploadForm
from .models import FileUpload

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import hashlib


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'contracts/signup.html'


def hashing(path):
	hasher = hashlib.md5()
	with open('./files/'+path, 'rb') as afile:
		buf = afile.read()
		hasher.update(buf)
		return hasher.hexdigest()


def index(request):
	if request.method == 'POST':
		form = FileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			selectFirst = FileUpload.objects.all().last()
			selectSecond = selectFirst.File
			conversionToString = str(selectSecond)
			fileHash = hashing(conversionToString)
			return HttpResponse(fileHash)
		else:
			return HttpResponse('Form NOT valid')

	else:
		form = FileUploadForm()
	return render(request, 'contracts/index.html', {'form': form})
