from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField


class RegisterModelForm(UserCreationForm):
    recaptcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "recaptcha"]
