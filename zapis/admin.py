from django.contrib import admin

from zapis.models import TodoItem


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("description", "is_completed", "created")
