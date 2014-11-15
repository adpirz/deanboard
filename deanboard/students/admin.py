from django.contrib import admin
from students.models import *

# Register your models here.


class ScholarAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'kbid', 'advisory')


class AdvisoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade')

admin.site.register(Scholar, ScholarAdmin)
admin.site.register(Advisory, AdvisoryAdmin)