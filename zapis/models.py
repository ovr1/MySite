from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class TodoItem(models.Model):
    objects = None
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "Массаж"),
        (PRIORITY_MEDIUM, "СПА"),
        (PRIORITY_LOW, "Медитация"),
    ]

    description = models.CharField(max_length=64)
    is_completed = models.BooleanField("выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="zapis")
    priority = models.IntegerField(
        "Приоритет", choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM
    )

    tags = TaggableManager()

    def __str__(self):
        return self.description.lower()

    class Meta:
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("zapis:details", args=[self.pk])
