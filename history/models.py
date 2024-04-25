from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

from .signals import object_viewed_signal
import uuid

User = settings.AUTH_USER_MODEL


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed: %s" %(self.query, self.created_at)

    class Meta:
        verbose_name_plural = "Histories"

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    new_history = History.objects.create(
        user    = request.user,
        query    = ContentType.objects.get_for_model(sender),
    )

object_viewed_signal.connect(object_viewed_receiver)