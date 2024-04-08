from django.urls import path
from .views import FactorListView, FactorACView

urlpatterns = [
  path('', FactorListView.as_view(), name='factor_list'),
  path('<uuid:pk>', FactorACView.as_view(), name='factor_ac'),
]