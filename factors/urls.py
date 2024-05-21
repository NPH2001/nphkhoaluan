from django.urls import path
from .views import FactorListView, FactorACView, SearchResultsListView,load

urlpatterns = [
  path('', FactorListView.as_view(), name='factor_list'),
  path('<uuid:pk>', FactorACView.as_view(), name='factor_ac'),
  path('search/', SearchResultsListView.as_view(), name='search_results'),
  path('load/', load, name='load'),
]