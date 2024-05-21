from django.contrib import admin

from .models import *

class SearchforcareAdmin(admin.ModelAdmin):
  list_display = ("sequences", "location_start", "location_end", "datetime")

admin.site.register(Searchforcare, SearchforcareAdmin)

class History_search_careAdmin(admin.ModelAdmin):
  list_display = ("id", "F_r", "R_f_r")

admin.site.register(History_search_care, History_search_careAdmin)