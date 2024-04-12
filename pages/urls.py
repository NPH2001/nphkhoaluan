from django.urls import path


from .views import HomePageView, AboutPageView, QueryCarePageView, SearchForCarePageView, GenesPageView, NameOfSitePageView, ReferenciaPageView, EnterNewDataPageView

urlpatterns = [
  path('about/', AboutPageView.as_view(), name='about'),
  path('genes/', GenesPageView.as_view(), name='genes'),
  path('referencia/', ReferenciaPageView.as_view(), name='referencia'),
  path('enternewdata/', EnterNewDataPageView.as_view(), name='enternewdata'),
  path('nameofsite/', NameOfSitePageView.as_view(), name='nameofsite'),
  path('querycare/', QueryCarePageView.as_view(), name='querycare'),
  path('searchforcare/', SearchForCarePageView.as_view(), name='searchforcare'),
  path('', HomePageView.as_view(), name='home'),
]
