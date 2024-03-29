from accounts.models import Profile, PhoneField
from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "last_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match")
        return cd["password2"]

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("p_num", "birthdate", "bio", "gip", "gipS", "var")




