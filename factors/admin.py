from django.contrib import admin

from .models import Factor

class FactorAdmin(admin.ModelAdmin):
  list_display = ("id", "ac", "dt", "de", "kw", "os", "ra", "rt", "rl", "rd", "sq", "color", "note")
  search_fields = ('id','ac','note',)
admin.site.register(Factor, FactorAdmin)
