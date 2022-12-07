from django.contrib import admin
from .models import (Task,List)
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('author', 'responsible','label', 'title', 'description', 'complete_status', 'created', 'deadline')
admin.site.register(Task, TaskAdmin)


class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'author')
admin.site.register(List, ListAdmin)