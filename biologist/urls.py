from django.urls import path

from .views import BiologistListView, BiologistDelete,Biologist_Create

urlpatterns = [
  path('delete/<int:pk>', BiologistDelete.as_view(), name='biologist_delete'),
  path('', BiologistListView.as_view(), name='biologist_list'),
  path('create/', Biologist_Create, name='Biologist_Create'),
]