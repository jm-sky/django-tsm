from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Image

# Create your views here.
def index(request):
  members = Member.objects.all()
  images = Image.objects.all()

  return render(request, 'pages/index.html', {
    'title': 'Welcome',
    'description': 'To jest strona DEMO',
    'members': members,
  })

# Create your views here.
def albums(request):
  images = Image.objects.all()
  images = images or [{ 'title': 'Test' }, { 'title': 'Mountains' }]

  return render(request, 'pages/albums.html', {
    'title': 'Album',
    'description': 'To jest przykładowy album ze zdjęciami. Dane idą z widoku. Nie da się tu nic zrobić na razie.',
    'images': images,
  })
