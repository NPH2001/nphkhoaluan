from django.contrib import admin

from .models import Factor

class FactorAdmin(admin.ModelAdmin):
  list_display = ("factor_id", "ac", "dt", "de", "kw", "os", "ra", "rt", "rl", "rd", "sq",)

admin.site.register(Factor, FactorAdmin)
