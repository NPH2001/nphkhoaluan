from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

from .models import History

def history_detail_query_care(request,pk):
    if request.method == 'GET':
        detail_list = History.objects.get(pk=pk)
        context = {'history_detail':detail_list}
        print('context:',context)
        return render(request, 'history/history_detail_query_care.html', context, status=200)
    
def history_detail_search_care(request,pk):
    if request.method == 'GET':
        detail_list = History.objects.get(pk=pk)
        Ms= detail_list.Belong_history_search_care.Ms.all()
        Ms=sorted(Ms, key=lambda i: len(i.sq), reverse=True)
        Ms_r= detail_list.Belong_history_search_care.Ms_r.all()
        Ms_r=sorted(Ms_r, key=lambda i: len(i.sq), reverse=True)
        context = {'history_detail':detail_list,'Ms':Ms,'Ms_r':Ms_r}
        print('context:',context)
        return render(request, 'history/history_detail_search_care.html', context, status=200)

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