from django.urls import path
from . import views
urlpatterns = [
  path('', views.MotifSampler, name='motifsampler_list'),
  path('result/', views.ResultMotif, name='motifsampler_result'),
]