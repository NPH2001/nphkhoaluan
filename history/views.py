from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

from .models import History

class HistoryList(ListView):
    model = History
    context_object_name = 'history_lists'
    def get_queryset(self):
        user_history = History.objects.filter(user=self.request.user).order_by('created_at')
        return user_history.reverse()
    
def return_to_search(request, pk):
    history_entry = History.objects.get(pk=pk)
    # Assuming the query is stored in the 'query' field of History model
    search_query = history_entry.query
    # Redirect to your search results view with the search query
    url_history = reverse('result_search_motif') + f'?sequencetosubmit={search_query}'
    url_history = reverse('search_results') + '?identifier=&accnumber=392&dateupdate=&briefdescription=&keywords=&os=&authorname=&titlereport=&bibliographic=&rd=&sequence='
    return redirect(url_history)


class HistoryDelete(SingleObjectMixin, View):
    model = History
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            obj.delete()
        return redirect('history')