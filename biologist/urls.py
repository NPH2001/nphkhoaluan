from django.urls import path

from .views import BiologistListView, BiologistDelete

urlpatterns = [
  path('delete/<int:pk>', BiologistDelete.as_view(), name='biologist_delete'),
  path('', BiologistListView.as_view(), name='biologist_list'),
]