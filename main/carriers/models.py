from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date


class Carriers(models.Model):
    organisation = models.CharField(max_length=200, help_text='Введите название организации', verbose_name='Название')
    form = [('ИПБОЮЛ', 'IPBUL'), ('ООО', 'ooo'), ('ОАО', 'oao'), ('3АО', 'zao'), ('ФИЗЛИЦО', 'fizik')]
    op_form = models.CharField(max_length=10, choices=form)
    # models.BooleanField(default=True, verbose_name='Наличие слота для карты SD')
    slug = models.SlugField(max_length=50)

    def is_upperclass(self):
        return self.op_form in {self.form[0][0], self.form[4][1]}

    def __str__(self):
        return self.organisation
