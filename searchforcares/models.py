from django.db import models
from django.urls import reverse
from factors.models import *

class Searchforcare(models.Model):
  sequences = models.CharField(max_length=200)
  location_start = models.CharField(max_length=200)
  location_end = models.CharField(max_length=200)
  datetime = models.DateTimeField()

  def __str__(self):
    return self.sequences
  
  def get_absolute_url(self): # new
    return reverse('motif_detail', args=[str(self.id)])
  

class History_search_care(models.Model):
  F_r = models.CharField(max_length=100000, null=True, blank=True)
  R_f_r = models.CharField(max_length=100000, null=True, blank=True)
  Ms= models.ManyToManyField(Factor, related_name='Ms_factor', blank=True)
  Ms_r = models.ManyToManyField(Factor, related_name='Ms_r_factor', blank=True)