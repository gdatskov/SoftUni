from django.contrib import admin

from djangoProject101.tasks.models import Task

# Variant 1 - customizable
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # pass # No customization yet
    list_display = ('id', 'name', 'description', 'priority')
# # Variant 2 - Simple
# admin.site.register(Task)
