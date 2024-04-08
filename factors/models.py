import uuid
from django.db import models
from django.urls import reverse

class Factor(models.Model):
  id = models.UUIDField( # new
      primary_key=True,
      default=uuid.uuid4,
      editable=False)
  factor_id = models.CharField(max_length=200)
  ac = models.CharField(max_length=200)
  dt = models.CharField(max_length=200)
  de = models.CharField(max_length=200)
  kw = models.CharField(max_length=200)
  os = models.CharField(max_length=200)
  ra = models.CharField(max_length=200)
  rt = models.CharField(max_length=200)
  rl = models.CharField(max_length=200)
  rd = models.CharField(max_length=200)
  sq = models.CharField(max_length=200)
  # dt = models.DecimalField(max_digits=6, decimal_places=2)

  
  def __str__(self):
    return self.factor_id
  
  def get_absolute_url(self):
    return reverse('factor_ac', args=[str(self.id)])