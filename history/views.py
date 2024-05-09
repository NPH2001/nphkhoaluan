from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin

from .models import History

class HistoryList(ListView):
    model = History
    context_object_name = 'history_lists'
    def get_queryset(self):
        user_history = History.objects.filter(user=self.request.user).order_by('created_at')
        return user_history.reverse()


class HistoryDelete(SingleObjectMixin, View):
    model = History
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            obj.delete()
        return redirect('history')