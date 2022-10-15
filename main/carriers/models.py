from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='',
        verbose_name=''
    )

    def __str__(self):
        return self.name
