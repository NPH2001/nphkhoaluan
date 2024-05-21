from django.urls import path

from .views import HistoryList, HistoryDelete, return_to_search,history_detail_query_care,history_detail_search_care

urlpatterns = [
    path('delete/<int:pk>', HistoryDelete.as_view(), name='history_delete'),
    path('history/<int:pk>/return/', return_to_search, name='return_to_search'),
    path('', HistoryList.as_view(), name='history'),
    path('history-detail-query-care/<int:pk>/', history_detail_query_care, name='history_detail_query_care'),
    path('history-detail-search-care/<int:pk>/', history_detail_search_care, name='history_detail_search_care'),
]