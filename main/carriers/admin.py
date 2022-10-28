from django.contrib import admin
from .models import *


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ['name_org', 'phone_org', 'email_org']
    search_fields = ['name_org']  # поиск
    list_filter = ('name_org',)  # фильтр
    # list_display_links = ['phone_org']  # ссылка

    fieldsets = (
        ('Общая информация', {
            'fields': ('name_org', 'org_form', 'carriers_type', 'phone_org', 'email_org')
        }),
        ('Контактное лицо', {
            'fields': ('first_name_cp', 'middle_name_cp', 'last_name_cp', 'position_cp', 'phone_cp', 'email_cp')
        }),
        ('Банковские реквизиты', {
            'fields': ('inn', 'ogrn', 'kpp', 'name_bank', 'ras_sch', 'cor_sch')
        }),
    )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_brand', 'vehicle_model', 'wheel_formula', 'vehicle_type', 'trailer_type']

    fieldsets = (
        ('Тягач', {
            'fields': ('carrier', 'vehicle_brand', 'vehicle_model', 'wheel_formula', 'vehicle_type',
                       'vehicle_colour', 'state_number_car', 'vin_number_car')
        }),
        ('Прицеп', {
            'fields': ('trailer_brand', 'trailer_type', 'state_number_trailer', 'vin_number_trailer',
                       'load_capacity', 'body_volume', 'bodywork')
        }),
    )


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']

    fieldsets = (
        ('', {
            'fields': ('carrier', 'first_name', 'middle_name', 'last_name', 'phone', 'email')
        }),
        ('Паспортные данные', {
            'fields': ('series_passport', 'number_passport', 'issued_by_passport',
                       'date_issue_passport', 'department_code')
        }),
        ('Водительское удостоверение', {
            'fields': ('series_driver_license', 'number_driver_license', 'issued_by_driver_license',
                       'date_issue_driver_license', 'validity_driver_license')
        }),
    )


admin.site.register(OrganizationalType)
admin.site.register(CarrierType)
admin.site.register(WheelFormula)
admin.site.register(VehicleColour)
admin.site.register(VehicleType)
admin.site.register(TrailerBrand)
admin.site.register(TrailerType)
