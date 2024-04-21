from django.urls import path

from .views import SearchMotif

urlpatterns = [
  path('searchmotif/', SearchMotif.as_view(), name='result_search_motif' ),
]
