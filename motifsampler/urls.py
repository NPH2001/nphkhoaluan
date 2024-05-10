from django.urls import path
from .views import MotifSamplerListView, ResultMotifSamplerListView
urlpatterns = [
  path('motifsampler_result/', ResultMotifSamplerListView.as_view(), name='motifsampler_result'),
  path('', MotifSamplerListView.as_view(), name='motifsampler_list'),

]