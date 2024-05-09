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
  de = models.TextField()
  kw = models.TextField()
  os = models.TextField()
  ra = models.TextField()
  rt = models.TextField()
  rl = models.TextField()
  rc = models.TextField()
  rd = models.TextField()
  sq = models.CharField(max_length=200)
  # dt = models.DecimalField(max_digits=6, decimal_places=2)

  
  def __str__(self):
    return self.factor_id
  
  def get_absolute_url(self):
    return reverse('factor_ac', args=[str(self.id)])