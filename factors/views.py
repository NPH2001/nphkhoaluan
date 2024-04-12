from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Factor

class FactorListView(ListView):
  model = Factor
  context_object_name = 'factor_list'
  template_name = 'factors/factor_list.html'


class FactorACView(DetailView):
  model = Factor
  context_object_name = 'factor'
  template_name = 'factors/factor_ac.html'


class SearchResultsListView(ListView): # new
  model = Factor
  context_object_name = 'factor_list'
  template_name = 'factors/search_results.html'

  def get_queryset(self):
      query_params = {
          'id': self.request.GET.get('identifier'),
          'ac': self.request.GET.get('accnumber'),
          'dt': self.request.GET.get('dateupdate'),  # Adjusted field name
          'de': self.request.GET.get('briefdescription'),
          'kw': self.request.GET.get('keywords'),
          'os': self.request.GET.get('os'),
          'ra': self.request.GET.get('authorname'),
          'rt': self.request.GET.get('titlereport'),
          'rl': self.request.GET.get('bibliographic'),
          'rd': self.request.GET.get('rd'),
          'sq': self.request.GET.get('sequence')
      }

      query_filters = {}
      for key, value in query_params.items():
          if value is not None:
              query_filters[key + '__icontains'] = value

      return Factor.objects.filter(**query_filters)

# contains: Phân biệt chữ hoa và chữ thường
# icontains: không phân biệt chữ hoa và chữ thường
# Q(ac__icontains=query) |
