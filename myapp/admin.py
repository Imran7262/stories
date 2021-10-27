from django.contrib import admin
from.models import *
admin.site.register(category)

class StudentAdmin(admin.ModelAdmin):
    list_display=('title','img','ctg','disc')
admin.site.register(photos,StudentAdmin)

class story(admin.ModelAdmin):
    list_display=('title','write')
admin.site.register(aply_for_story,story)
