from django.contrib.auth.models import User
from django.db import models


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birthdate = models.DateField(blank=True, null=True)
    description = models.TextField(default='Пожелание')
    mail = models.EmailField(max_length=120)
    phone_number = models.CharField(max_length=12)
    visible = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "Профиль пользователя %s" % self.user

    class Meta:
        ordering = ["-id", "-timestamp"]


# Create your models here.

