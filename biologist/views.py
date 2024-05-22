from django.contrib.auth.mixins import (
  LoginRequiredMixin,
  PermissionRequiredMixin # new
)


from django.views.generic import ListView, View
from .models import Biologist
from django.shortcuts import render, redirect
from django.views.generic.detail import SingleObjectMixin
from factors.models import *
import random

def random_color():
  # Tạo các giá trị ngẫu nhiên cho R, G, B
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  # Trả về màu dưới dạng mã hex
  return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def Biologist_Create(request):
    if request.method == 'GET':
        data = request.GET.get('data')
        id = request.GET.get('id')
        context = {'data':data,'id':id}
        return render(request, 'biologist/biologist_create.html', context, status=200)
    if request.method == 'POST':
        id_confim = request.POST.get('id_confim')
        ac = request.POST.get('ac')
        print('ac:',ac)
        dt = request.POST.get('dt')
        de = request.POST.get('de')
        print('de:',de)
        kw = request.POST.get('kw')
        os = request.POST.get('os')
        ra = request.POST.get('ra')
        rt = request.POST.get('rt')
        rl = request.POST.get('rl')
        rd = request.POST.get('rd')
        sq = request.POST.get('sq')
        print('sq:',sq)
        ff = Factor.objects.create(ac=ac,dt=dt,de=de,kw=kw,os=os,ra=ra,rt=rt,rl=rl,rd=rd,sq=sq,color = random_color(),note='computational motif')
        print('ff:',ff)
        bg = Biologist.objects.get(pk=int(id_confim))
        bg.delete()
        # Chuyển hướng đến trang thành công hoặc trang khác
        return redirect('biologist_list')

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
