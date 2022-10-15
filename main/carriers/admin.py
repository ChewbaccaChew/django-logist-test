from django.contrib import admin
from carriers.models import Carriers


# admin.site.register(Carriers)
@admin.register(Carriers)
class CarriersAdmin(admin.ModelAdmin):
    list_display = ['organisation', 'op_form']
    prepopulated_fields = {'slug': ('organisation',)}
