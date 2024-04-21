from django.contrib import admin

from .models import Searchforcare

class SearchforcareAdmin(admin.ModelAdmin):
  list_display = ("sequences", "location_start", "location_end", "datetime")

admin.site.register(Searchforcare, SearchforcareAdmin)