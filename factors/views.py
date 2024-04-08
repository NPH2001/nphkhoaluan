from django.views.generic import ListView, DetailView

from .models import Factor

class FactorListView(ListView):
  model = Factor
  context_object_name = 'factor_list'
  template_name = 'factors/factor_list.html'


class FactorACView(DetailView):
  model = Factor
  context_object_name = 'factor'
  template_name = 'factors/factor_ac.html'
