from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date


class Carrier(models.Model):
    """Модель Перевозчика"""

    # models.BooleanField(default=True, verbose_name='Наличие слота для карты SD')
    organisation = models.CharField(
        max_length=200,
        help_text='Введите название организации',
        verbose_name='Название',
    )

    form = [
        ('IPBUL', 'ИПБОЮЛ'),
        ('OOO', 'ООО'),
        ('OAO', 'ОАО'),
        ('ZAO', '3АО'),
        ('FIZIK', 'ФИЗЛИЦО'),
    ]

    op_form = models.CharField(
        max_length=10,
        choices=form,
        null=True,
        help_text='Организационно-правовая форма',
        verbose_name='ОПФ',
    )

    slug = models.SlugField(
        max_length=50,
        help_text='Сделать автоматическим',
        verbose_name='Слаг',
    )

    phone_org = models.CharField(
        max_length=20,
        null=True,
        help_text='Введите основной номер телефона',
        verbose_name='Номер телефона',
    )

    email = models.CharField(
        max_length=100,
        null=True,
        help_text='Введите адрес электронной почты',
        verbose_name='Email',
    )

    type = [
        ('PEREVOZ', 'ПЕРЕВОЗЧИК'),
        ('EKS_PEREVOZ', 'ЭКСПЕДИТОР-ПЕРЕВОЗЧИК'),
        ('EKS', 'ЭКСПЕДИТОР'),
        ('OWNER', 'ГРУЗОВЛАДЕЛЕЦ'),
        ('OTPRAV', 'ГРУЗООТПРАВИТЕЛЬ'),
        ('POLUCH', 'ГРУЗОПОЛУЧАТЕЛЬ'),
        ('OTHER_TYPE', 'ДРУГОЙ ВАРИАНТ'),
    ]

    carrier_type = models.CharField(
        max_length=50,
        choices=type,
        null=True, blank=True,
        help_text='Введите тип перевозчика',
        verbose_name='Тип перевозчика',
    )

    # bank_info
    inn = models.CharField(
        max_length=100,
        help_text='Введите номер ИНН',
        verbose_name='ИНН расшифровать',
    )

    ogrn = models.CharField(
        max_length=100,
        help_text='Введите номер ОГРН',
        verbose_name='ОГРН расшифровать',
    )

    kpp = models.CharField(
        max_length=100,
        help_text='Введите номер КПП',
        verbose_name='КПП расшифровать',
    )

    bank_name = models.CharField(
        max_length=100,
        help_text='Введите название банка',
        verbose_name='Банк',
    )

    ras_sch = models.CharField(
        max_length=100,
        help_text='Введите номер расчетного счета',
        verbose_name='Р/сч',
    )

    cor_sch = models.CharField(
        max_length=100,
        help_text='Введите номер корпоративного счета',
        verbose_name='Кор/сч',
    )

    # End bank_info

    # contact_person
    fio = models.CharField(
        max_length=100,
        null=True,
        help_text='Введите ФИО',
        verbose_name='Фамилия Имя Отчество',
    )

    phone_contact_person = models.CharField(
        max_length=20,
        null=True,
        help_text='Введите номер контактного телефона',
        verbose_name='Номер контактного телефона',
    )

    email_contact_person = models.CharField(
        max_length=100,
        null=True,
        help_text='Введите адрес электронной почты',
        verbose_name='Email',
    )

    position = models.CharField(
        max_length=100,
        null=True,
        help_text='Введите должность',
        verbose_name='Должность',
    )

    # End contact_person

    def __str__(self):
        return self.organisation


class Car(models.Model):
    """Модель Транспортного средства (ТС)"""

    # tyagach
    brand_car = models.CharField(
        max_length=100,
        help_text='Введите марку ТС',
        verbose_name='Марка Транспортного Средства',
    )

    slug = models.SlugField(
        max_length=50,
        null=True,
        help_text='Сделать автоматическим',
        verbose_name='Слаг',
    )

    state_number = models.CharField(
        max_length=10,
        help_text='Введите государственный номер ТС',
        verbose_name='Гос/номер ТС',
    )

    vin_number = models.CharField(
        max_length=50,
        help_text='Введите VIN номер ТС',
        verbose_name='VIN/номер ТС',
    )

    formula = [
        ('2', '2x2'),
        ('4', '4x4'),
        ('8', '8x8'),
    ]

    wheel_formula = models.CharField(
        max_length=50,
        choices=formula,
        help_text='Введите VIN номер ТС',
        verbose_name='VIN/номер ТС',
    )

    colour_list = [
        ('RED', 'Красный'),
        ('WHITE', 'Белый'),
        ('BLUE', 'Синий'),
        ('GREEN', 'Зеленый'),
    ]

    colour = models.CharField(
        max_length=50,
        choices=colour_list,
        help_text='Введите цвет ТС',
        verbose_name='Цвет ТС',
    )

    type_car_list = [
        ('takoi', 'Такой'),
        ('syakoi', 'Сякой'),
        ('takoi', 'Такой'),
        ('syakoi', 'Сякой'),
    ]

    type_car = models.CharField(
        max_length=50,
        choices=type_car_list,
        help_text='Введите цвет ТС',
        verbose_name='Цвет ТС',
    )

    # End tyagach

    # polupricep
    brand_pricepa = models.CharField(
        max_length=100,
        help_text='Введите марку Прицепа',
        verbose_name='Марка Прицепа',
    )

    state_number_pricepa = models.CharField(
        max_length=10,
        help_text='Введите государственный номер Прицепа',
        verbose_name='Гос/номер Прицепа',
    )

    vin_number_pricepa = models.CharField(
        max_length=50,
        help_text='Введите VIN номер Прицепа',
        verbose_name='VIN/номер Прицепа',
    )

    load_capacity = models.CharField(
        max_length=10,
        help_text='Введите грузоподъемность Прицепа',
        verbose_name='Грузоподъемность Прицепа',
    )

    bodywork = models.CharField(
        max_length=20,
        help_text='Введите габариты кузова',
        verbose_name='Габариты кузова',
    )

    body_volume = models.CharField(
        max_length=10,
        help_text='Введите объем кузова',
        verbose_name='Объем кузова',
    )

    type_pricepa_list = [
        ('takoi', 'Такой'),
        ('syakoi', 'Сякой'),
        ('takoi', 'Такой'),
        ('syakoi', 'Сякой'),
    ]

    type_pricepa = models.CharField(
        max_length=50,
        choices=type_pricepa_list,
        help_text='Введите тип Прицепа',
        verbose_name='Тип Прицепа',
    )

    # End polupricep

    def __str__(self):
        return self.brand_car


class Driver(models.Model):
    """ Модель Водителя """

    # foto
    # pasport(seriya, number, kem_vidan, date_vidachi, kod_podrazdeleniya)
    # voditelskoe_udostoverenie(seriya, number, kem_vidan, date_vidachi, date_okonchaniya_deistviya)

    slug = models.SlugField(
        max_length=50,
        null=True,
        help_text='Сделать автоматическим',
        verbose_name='Слаг',
    )

    fio_driver = models.CharField(
        max_length=100,
        null=True,
        help_text='Введите ФИО',
        verbose_name='Фамилия Имя Отчество',
    )

    phone_driver = models.CharField(
        max_length=20,
        null=True,
        help_text='Введите номер контактного телефона',
        verbose_name='Номер контактного телефона',
    )

    email_driver = models.CharField(
        max_length=100,
        null=True,
        help_text='Введите адрес электронной почты',
        verbose_name='Email',
    )

    def __str__(self):
        return self.fio_driver
