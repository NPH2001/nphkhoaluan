from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class QueryCarePageView(TemplateView):
    template_name = 'querycare.html'

class SearchForCarePageView(TemplateView):
    template_name = 'searchforcare.html'

class GenesPageView(TemplateView):
    template_name = 'genes.html'

class NameOfSitePageView(TemplateView):
    template_name = 'nameofsite.html'

class ReferenciaPageView(TemplateView):
    template_name = 'referencia.html'

class EnterNewDataPageView(TemplateView):
    template_name = 'enternewdata.html'

# class PageView(TemplateView):
#     template_name = '.html'
    
