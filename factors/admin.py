from django.contrib import admin

from .models import Factor, FunctionLabels

class FunctionLabelsAdmin(admin.ModelAdmin):
  list_display = ("id", "label", "detail_label")
  search_fields = ('id','label','detail_label')

class FactorAdmin(admin.ModelAdmin):
  list_display = ("id", "ac", "dt", "de", "kw", "os", "ra", "rt", "rl", "rd", "sq", "color", "note", "ft")
  search_fields = ('id','ac','note','ft', 'sq')
  

admin.site.register(Factor, FactorAdmin)
admin.site.register(FunctionLabels, FunctionLabelsAdmin)
