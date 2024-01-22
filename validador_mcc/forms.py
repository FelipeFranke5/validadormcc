from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError
from .models import RestrictedMcc


class RestrictedMccModelForm(forms.ModelForm):
    recaptcha = ReCaptchaField()

    class Meta:
        model = RestrictedMcc
        fields = ["name", "code", "recaptcha"]

    def clean_code(self):
        code = self.cleaned_data["code"]

        if len(str(code)) < 4 or len(str(code)) > 4:
            raise ValidationError("The mcc code should have 4 digits (xxxx)")
        return code
