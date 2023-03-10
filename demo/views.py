from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Image

# Create your views here.
def index(request):
  members = Member.objects.all()
  images = Image.objects.all()

  return render(request, 'layouts/main.html', {
    'title': 'Welcome',
    'page': 'index.html',
    'description': 'To jest strona DEMO',
    'members': members,
  })

# Create your views here.
def albums(request):
  images = Image.objects.all()
  images = images or [{ 'title': 'Test' }, { 'title': 'Mountains' }]

  return render(request, 'layouts/main.html', {
    'title': 'Album',
    'page': 'pages/albums.html',
    'description': 'To jest przykładowy album ze zdjęciami. Dane idą z widoku. Nie da się tu nic zrobić na razie.',
    'images': images,
  })
