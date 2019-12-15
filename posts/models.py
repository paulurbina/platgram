from django.db import models

class User(models.Model):
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=100)

  firt_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

  bio = models.TextField()

  birhdate = models.DateField(blank=True, null=True)

  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)