from django.urls import path

from .views import HistoryList, HistoryDelete, return_to_search

urlpatterns = [
    path('delete/<int:pk>', HistoryDelete.as_view(), name='history_delete'),
    path('history/<int:pk>/return/', return_to_search, name='return_to_search'),
    path('', HistoryList.as_view(), name='history'),
]