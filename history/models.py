from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

from .signals import object_viewed_signal
import uuid

from factors.models import *
from searchforcares.models import *

User = settings.AUTH_USER_MODEL


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    Belong_factor = models.ManyToManyField(Factor, related_name='belong_factor', blank=True)
    Belong_history_search_care = models.ForeignKey(History_search_care, on_delete=models.CASCADE,related_name='belong_history_search_care',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed: %s" %(self.query, self.created_at)

    class Meta:
        verbose_name_plural = "Histories"

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    query_filters = ContentType.objects.get_for_model(sender)
    print('query_filters1:',query_filters)
    factor_list = Factor.objects.filter(**query_filters)
    print('factor_list1:',factor_list)
    new_history = History.objects.create(
        user    = request.user,
        query    = ContentType.objects.get_for_model(sender),
    )
    print('new_history:',new_history)
    new_history.Belong_factor.set(factor_list)
    new_history.save()

object_viewed_signal.connect(object_viewed_receiver)