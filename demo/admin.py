from django.contrib import admin
from .models import Member
from .models import Image

# Register your models here.
admin.site.register(Member)
admin.site.register(Image)
