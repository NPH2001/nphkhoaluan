from django.urls import path
from . import views
from .views import MotifSamplerListView, ResultMotifSamplerListView
urlpatterns = [
  path('result/', ResultMotifSamplerListView.simple_upload, name='motifsampler_result'),
  path('', MotifSamplerListView.as_view(), name='motifsampler_list'),

]