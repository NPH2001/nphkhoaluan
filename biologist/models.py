import uuid
from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Biologist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  sequences = models.CharField(max_length=200)
  def __str__(self):
    return self.sequences
  
  class Meta: # new
    permissions = [
      ('special_status', 'Can confirm motifs'),
    ]