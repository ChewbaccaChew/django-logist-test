from django.db import models


class OrganizationalForm(models.Model):
    """Модель - ОПФ"""

    name = models.CharField(max_length=10, help_text='Введите организационно-правовую форму', verbose_name='ОПФ')

    def __str__(self):
        return self.name


class CarrierType(models.Model):
    """Модель - Тип перевозчика"""

    name = models.CharField(max_length=50, verbose_name='Тип перевозчика')

    def __str__(self):
        return self.name


class Carrier(models.Model):
    """Модель - Перевозчик"""

    class Meta:
        verbose_name_plural = 'Перевозчики'
        verbose_name = 'Перевозчикa'
        ordering = ['name_org']

    name_org = models.CharField(max_length=200, verbose_name='Название организации')
    org_form = models.ForeignKey('OrganizationalForm', null=True, verbose_name='ОПФ', on_delete=models.CASCADE)
    carriers_type = models.ForeignKey('CarrierType', null=True, verbose_name='Тип перевозчика', on_delete=models.CASCADE)
    phone_org = models.CharField(max_length=20, verbose_name='Номер телефона')
    email_org = models.CharField(max_length=100, verbose_name='Email')

    # contact_person
    first_name_cp = models.CharField(max_length=100, help_text='Введите имя контактного лица', verbose_name='Имя')
    middle_name_cp = models.CharField(max_length=100, verbose_name='Отчество')
    last_name_cp = models.CharField(max_length=100, verbose_name='Фамилия')
    phone_cp = models.CharField(max_length=20, verbose_name='Контактный телефон')
    email_cp = models.CharField(max_length=100, verbose_name='Email')
    position_cp = models.CharField(max_length=100, help_text='Введите должность контактного лица', verbose_name='Должность')

    # bank_info
    inn = models.CharField(max_length=100, help_text='ИНН расшифровать', verbose_name='ИНН')
    ogrn = models.CharField(max_length=100, help_text='ОГРН расшифровать', verbose_name='ОГРН')
    kpp = models.CharField(max_length=100, help_text='КПП расшифровать', verbose_name='КПП')
    name_bank = models.CharField(max_length=100, help_text='Введите название банка', verbose_name='Банк')
    ras_sch = models.CharField(max_length=100, help_text='Введите номер расчетного счета', verbose_name='Р/сч')
    cor_sch = models.CharField(max_length=100, help_text='Введите номер корпоративного счета', verbose_name='Кор/сч')

    def __str__(self):
        return self.name_org


class WheelFormula(models.Model):
    """Модель - Колесная формула"""

    name = models.CharField(max_length=10, verbose_name='Колесная формула')

    def __str__(self):
        return self.name


class VehicleColour(models.Model):
    """Модель - Цвет ТС"""

    name = models.CharField(max_length=50, verbose_name='Цвет ТС')

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    """Модель - Тип ТС"""

    name = models.CharField(max_length=50, verbose_name='Тип ТС')

    def __str__(self):
        return self.name


class VehicleBrand(models.Model):
    """Модель - Марка ТС"""

    name_brand = models.CharField(max_length=100, verbose_name='Марка Транспортного Средства')
    name_model = models.CharField(max_length=100, verbose_name='Модель Транспортного Средства')

    def __str__(self):
        return self.name_brand, self.name_model


class TrailerBrand(models.Model):
    """Модель - Марка прицепа"""

    name = models.CharField(max_length=100, verbose_name='Марка Прицепа')

    def __str__(self):
        return self.name


class TrailerType(models.Model):
    """Модель - Тип прицепа"""

    name = models.CharField(max_length=50, verbose_name='Тип Прицепа')

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    """Модель - Транспортное средство (ТС)"""

    class Meta:
        verbose_name_plural = 'Транспортные средства'
        verbose_name = 'Транспортное средство'

    # tractor
    vehicle_brand = models.ForeignKey('VehicleBrand', null=True, verbose_name='Марка и Модель ТС', on_delete=models.CASCADE)
    state_number_car = models.CharField(max_length=10, verbose_name='Гос/номер ТС')
    vin_number_car = models.CharField(max_length=50, verbose_name='VIN/номер ТС')
    wheel_formula = models.ForeignKey('WheelFormula', null=True, verbose_name='Колесная формула', on_delete=models.CASCADE)
    vehicle_colour = models.ForeignKey('VehicleColour', null=True, verbose_name='Цвет ТС', on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey('VehicleType', null=True, verbose_name='Тип ТС', on_delete=models.CASCADE)

    # trailer
    state_number_trailer = models.CharField(max_length=10, verbose_name='Гос/номер Прицепа')
    vin_number_trailer = models.CharField(max_length=50, verbose_name='VIN/номер Прицепа')
    load_capacity = models.CharField(max_length=10, verbose_name='Грузоподъемность Прицепа')
    body_volume = models.CharField(max_length=10, verbose_name='Объем кузова')
    bodywork = models.CharField(max_length=20, verbose_name='Габариты кузова')
    trailer_brand = models.ForeignKey('TrailerBrand', null=True, verbose_name='Марка прицепа', on_delete=models.CASCADE)
    trailer_type = models.ForeignKey('TrailerType', null=True, verbose_name='Тип прицепа', on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_brand


class Driver(models.Model):
    """ Модель Водитель """

    class Meta:
        verbose_name_plural = 'Водители'
        verbose_name = 'Водителя'

    # photo =
    first_name = models.CharField(max_length=100, verbose_name='Имя водителя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Контактный телефон')
    email = models.CharField(max_length=100, verbose_name='Email')

    # passport(серия, номер, кем выдан, дата выдачи, код подразделения)
    series_passport = models.CharField(max_length=10, verbose_name='Серия паспорта')
    number_passport = models.CharField(max_length=20, verbose_name='Номер паспорта')
    issued_by_passport = models.CharField(max_length=200, verbose_name='Кем выдан')
    date_issue_passport = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')
    department_code = models.CharField(max_length=20, verbose_name='Код подразделения')

    # driver_license(серия, номер, кем выдан, дата выдачи, дата окончания действия)
    series_driver_license = models.CharField(max_length=10, verbose_name='Серия водительского')
    number_driver_license = models.CharField(max_length=20, verbose_name='Номер водительского')
    issued_by_driver_license = models.CharField(max_length=200, verbose_name='Кем выдан')
    date_issue_driver_license = models.DateField(null=True, blank=True, verbose_name='Дата выдачи')
    validity_driver_license = models.DateField(null=True, blank=True, verbose_name='Дата окончания действия')

    def __str__(self):
        return self.last_name
