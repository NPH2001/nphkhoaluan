from django.contrib import admin

from .models import History

class HistoryAdmin(admin.ModelAdmin):
  list_display = ("query", "created_at")

admin.site.register(History, HistoryAdmin)