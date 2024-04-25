from .signals import object_viewed_signal
from .models import History

class ObjectViewMixin:
    def record_search_history(self, query, user):
        if user and hasattr(user, 'is_authenticated') and user.is_authenticated:
            History.objects.create(user=user, query=query)

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
    