from django.urls import path

from .views import SearchMotif,Detail_ac

urlpatterns = [
  path('searchmotif/', SearchMotif.as_view(), name='result_search_motif' ),
  path('history-detail-search-care/<uuid:pk>/', Detail_ac, name='Detail_ac'),
  path('export-csv/', SearchMotif.export_csv_by_current_result, name='export_csv'),
  path('export-rev-csv/', SearchMotif.export_csv_by_current_rev_result, name='export_rev_csv'),
]
