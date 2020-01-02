from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select

class PhoneWidget(MultiWidget):
    objects = None
    def __init__(self, code_length=3, num_length=7, attrs=None):
        widgets = [TextInput(attrs={'size': code_length, 'maxlength': code_length}),
                   TextInput(attrs={'size': num_length, 'maxlength': num_length})]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.number]
        else:
            return ['', '']

    def format_output(self, rendered_widgets):
        return '+7' + '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]

class PhoneField(MultiValueField):
    objects = None

    def __init__(self, code_length, num_length, *args, **kwargs):
        list_fields = [CharField(),
                       CharField()]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

    def compress(self, values):
        return '+7' + values[0] + values[1]  #Собственно, стандартизация строки номера эстетики ради


class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    p_num = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Номер телефона')
    birthdate = models.DateField(blank=True, null=True, verbose_name = 'День рождение' )
    bio = models.BooleanField(blank=True, null=True, verbose_name = 'Хронические заболевания' )
    gip = models.BooleanField(blank=True, null=True, verbose_name = 'Гипертония' )
    gipS = models.CharField(max_length=1, blank=True, null=True, verbose_name = 'Степень гипертонии')
    var = models.BooleanField(blank=True, null=True, verbose_name = 'Варикозное расширение вен, нижних конечностей' )


    def __str__(self):
        return "Профиль пользователя %s" % self.user.username

@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)


# Create your models here.
