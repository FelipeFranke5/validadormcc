from django.db import models


class RestrictedMcc(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.name
