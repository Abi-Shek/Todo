from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_compeleted','updated_ad')
    search_fields = ('task',)
admin.site.register(Task,TaskAdmin)