from .signals import object_viewed_signal
from .models import History
from factors.models import *

class ObjectViewMixin:
    def record_search_history(self, query, user,value_query_filter):
        if user and hasattr(user, 'is_authenticated') and user.is_authenticated:
            if value_query_filter:
                factor_list = Factor.objects.filter(**value_query_filter)
                print('factor_list1:',factor_list)
                new_history = History.objects.create(user=user, query=query)
                new_history.Belong_factor.set(factor_list)
                new_history.save()
            else:
                pass

class ObjectViewMixin1:
    def dispatch(self, request, *args, **kwargs):
        if hasattr(self, 'get_object'):
            try:
                instance = self.get_object()
            except self.model.DoesNotExist:
                instance = None
        else:
            instance = None
        
        if request.user.is_authenticated and instance is not None:
            object_viewed_signal.send(instance.__class__, instance=instance, request=request)

        return super(ObjectViewMixin1, self).dispatch(request, *args, **kwargs)
    