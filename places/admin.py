from django.contrib import admin

from places.models import Regions

class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Regions, RegionAdmin)
