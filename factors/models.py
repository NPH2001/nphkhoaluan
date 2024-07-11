import uuid
from django.db import models
from django.urls import reverse

class FunctionLabels(models.Model):
  id = models.UUIDField( # new
      primary_key=True,
      default=uuid.uuid4,
      editable=False)
  label = models.CharField(max_length=200,null=True, blank=True)
  detail_label = models.CharField(max_length=200,null=True, blank=True)
  
  def __str__(self):
    return self.label
  
class Factor(models.Model):
  id = models.UUIDField( # new
      primary_key=True,
      default=uuid.uuid4,
      editable=False)
  ac = models.CharField(max_length=200,null=True, blank=True)
  dt = models.CharField(max_length=200,null=True, blank=True)
  de = models.TextField(null=True, blank=True)
  kw = models.TextField(null=True, blank=True)
  os = models.TextField(null=True, blank=True)
  ra = models.TextField(null=True, blank=True)
  rt = models.TextField(null=True, blank=True)
  rl = models.TextField(null=True, blank=True)
  rc = models.TextField(null=True, blank=True)
  rd = models.TextField(null=True, blank=True)
  sq = models.CharField(max_length=200,null=True, blank=True)
  color = models.CharField(max_length=200,null=True, blank=True)
  note = models.CharField(max_length=100, null=True, blank=True)
  ft = models.ForeignKey(FunctionLabels, on_delete=models.CASCADE, null=True, blank=True)
  # dt = models.DecimalField(max_digits=6, decimal_places=2)

  
  def __str__(self):
    return str(self.id)
  
  def get_absolute_url(self):
    return reverse('factor_ac', args=[str(self.id)])
  
