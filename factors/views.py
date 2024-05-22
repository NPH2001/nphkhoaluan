from django.views.generic import ListView, DetailView

from .models import Factor

from history.mixins import ObjectViewMixin
import json
from django.http import HttpResponse
import random

def random_color():
  # Tạo các giá trị ngẫu nhiên cho R, G, B
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  # Trả về màu dưới dạng mã hex
  return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def load(request):
  if request.method == 'GET':
    with open('db.json', 'r') as file:
        a = json.load(file)
    for i in a :
      Factor.objects.create(ac=i['fields']['ac'],
                            dt=i['fields']['dt'],
                            de=i['fields']['de'],
                            kw=i['fields']['kw'],
                            os=i['fields']['os'],
                            ra=i['fields']['ra'],
                            rt=i['fields']['rt'],
                            rl=i['fields']['rl'],
                            rc=i['fields']['rc'],
                            rd=i['fields']['rd'],
                            sq=i['fields']['sq'],
                            color = random_color()
                            )
    return HttpResponse("Nạp dữ liệu thành công", status=200)

class FactorListView(ListView):
  model = Factor
  context_object_name = 'factor_list'
  template_name = 'factors/factor_list.html'


class FactorACView(DetailView):
  model = Factor
  context_object_name = 'factor'
  template_name = 'factors/factor_ac.html'


class SearchResultsListView(ObjectViewMixin, ListView): # new
  model = Factor
  context_object_name = 'factor_list'
  template_name = 'factors/search_results.html'


  def get_query_params(self):
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
          if value is not None and value != '':
              query_filters[key + '__icontains'] = value
      return query_filters
  
  def dispatch(self, request, *args, **kwargs):
      value_query_filter = self.get_query_params()
      for key, value in value_query_filter.items():
         if key == 'id__icontains':
          query = 'identifier: ' + value
         elif key == 'ac__icontains':
          query = 'accnumber: ' + value
         elif key == 'dt__icontains':
          query = 'dateupdate: ' + value
         elif key == 'de__icontains':
          query = 'briefdescription: ' + value
         elif key == 'kw__icontains':
          query = 'keywords: ' + value
         elif key == 'os__icontains':
          query = 'os: ' + value
         elif key == 'ra__icontains':
          query = 'authorname: ' + value
         elif key == 'rt__icontains':
          query = 'titlereport: ' + value
         elif key == 'rl__icontains':
          query = 'bibliographic: ' + value
         elif key == 'rd__icontains':
          query = 'rd: ' + value
         elif key == 'sq__icontains':
          query = 'sequence: ' + value
            

      # Lấy thông tin tìm kiếm từ request
      user = request.user if request.user.is_authenticated else None  # Lấy thông tin người dùng
      if query is not None:
        self.record_search_history(query, user,value_query_filter)
      return super().dispatch(request, *args, **kwargs)
  
  def get_queryset(self):
     query_filters = self.get_query_params()
     factor_list = Factor.objects.filter(**query_filters)
     print('factor_list:',factor_list)
     return factor_list
  
# contains: Phân biệt chữ hoa và chữ thường
# icontains: không phân biệt chữ hoa và chữ thường
