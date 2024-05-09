from django.contrib.auth.mixins import (
  LoginRequiredMixin,
  PermissionRequiredMixin # new
)


from django.views.generic import ListView, View
from .models import Biologist
from django.shortcuts import render, redirect
from django.views.generic.detail import SingleObjectMixin

class BiologistListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
  model = Biologist
  template_name = 'biologist/biologist_list.html'
  login_url = 'account_login'
  permission_required = 'biologist.special_status'


# class BiologistConfirm(ListView):
#   def get_one_view(request, sequences):
   
#     Biologist.objects.create(one_id = sequences)        

#     return render(request, "biologist_list.html", {})

class BiologistDelete(SingleObjectMixin, View):
    model = Biologist
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            obj.delete()
        return redirect('biologist_list')
