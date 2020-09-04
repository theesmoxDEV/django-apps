from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from djangoProject.settings import MEDIA_URL
from .models import ChatFile


# Create your views here.

def index(request):
    return render(request, 'base.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_cloud')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


def create_cloud(request):
    doc = ChatFile.objects.last()
    doc.create_cloud()
    wordcloud_name = doc.wordcloud_name
    return render(request, 'cloud.html', {'wordcloud_name': wordcloud_name})
