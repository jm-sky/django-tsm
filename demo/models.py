from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    birth_date = models.DateField(null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Image(models.Model):
    title: models.CharField(max_length=100)
    description: models.CharField(max_length=500)
    url: models.URLField(max_length=100)

    def __str__(self):
        return self.title
