from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Image

# Create your views here.
def index(request):
  members = Member.objects.all()
  images = Image.objects.all()

  return render(request, 'layouts/main.html', {
    'title': 'Album',
    'description': 'To jest przykładowy album ze zdjęciami. Dane idą z widoku. Nie da się tu nic zrobić na razie.',
    'members': members,
    'images': images,
  })
