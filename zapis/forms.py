from django import forms
from zapis.models import TodoItem


class AddTaskForm(forms.Form):
    description = forms.CharField(max_length=64, label="")


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ("description", "priority", "tags")
        labels = {"description": "Описание", "priority": "", "tags": "тэги"}


class TodoItemExportForm(forms.Form):
    prio_high = forms.BooleanField(
        label="массаж", initial=True, required=False
    )
    prio_med = forms.BooleanField(
        label="спа", initial=True, required=False
    )
    prio_low = forms.BooleanField(
        label="медитация", initial=False, required=False
    )