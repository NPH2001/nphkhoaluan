from django.db import models
from django.urls import reverse


class Searchforcare(models.Model):
  sequences = models.CharField(max_length=200)
  location_start = models.CharField(max_length=200)
  location_end = models.CharField(max_length=200)
  datetime = models.DateTimeField()

  def __str__(self):
    return self.sequences
  
  def get_absolute_url(self): # new
    return reverse('motif_detail', args=[str(self.id)])