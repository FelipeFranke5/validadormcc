import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class NumberValidator:
    def validate(self, password: str, user: str):
        if not re.findall(r"\d", password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code="password_number_required",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 digit, 0-9.")


class UppercaseValidator:
    def validate(self, password: str, user: str):
        if not re.findall(r"[A-Z]", password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code="password_upper_required",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 uppercase letter, A-Z.")


class LowercaseValidator:
    def validate(self, password: str, user: str):
        if not re.findall(r"[a-z]", password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code="password_lower_required",
            )

    def get_help_text(self):
        return _("Your password must contain at least 1 lowercase letter, a-z.")


class SymbolValidator:
    def validate(self, password: str, user: str):
        if not re.findall(r"[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]", password):
            raise ValidationError(
                _(
                    "The password must contain at least 1 symbol: "
                    + r"()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
                ),
                code="password_symbol_required",
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: "
            + r"()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
