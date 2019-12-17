from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  """ Profile model.
    Proxy models that extenst the base data woith other information
  """
  user =  models.OneToOneField(User, on_delete=models.CASCADE)

  website = models.URLField(max_length=200, blank=True)
  bigoraphy = models.TextField(blank=True)
  phone_number = models.CharField(max_length=20, blank=True)

  picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username