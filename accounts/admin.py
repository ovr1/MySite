from django.contrib import admin

from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "p_num", "birthdate", "bio", "gip", "gipS", "var", "sex"]


# Register your models here.
