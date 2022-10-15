from django.contrib import admin
from carriers.models import Carrier, Car


# admin.site.register(Carrier)
@admin.register(Carrier)
class CarriersAdmin(admin.ModelAdmin):
    list_display = ['organisation', 'op_form']
    prepopulated_fields = {'slug': ('organisation',)}


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand_car', 'type_car']
    prepopulated_fields = {'slug': ('brand_car',)}
