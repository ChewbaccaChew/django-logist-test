from django.forms import ModelForm

from .models import (
    Carrier,
    Vehicle,
    Driver,
    OrganizationalType,
    CarrierType,
    WheelFormula,
    VehicleColour,
    VehicleType,
    TrailerBrand,
    TrailerType,
)


class CarriersForm(ModelForm):
    class Meta:
        model = Carrier
        fields = '__all__'


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'


class OrganizationalTypeForm(ModelForm):
    class Meta:
        model = OrganizationalType
        fields = '__all__'


class CarrierTypeForm(ModelForm):
    class Meta:
        model = CarrierType
        fields = '__all__'


class WheelFormulaForm(ModelForm):
    class Meta:
        model = WheelFormula
        fields = '__all__'


class VehicleColourForm(ModelForm):
    class Meta:
        model = VehicleColour
        fields = '__all__'


class VehicleTypeForm(ModelForm):
    class Meta:
        model = VehicleType
        fields = '__all__'


class TrailerBrandForm(ModelForm):
    class Meta:
        model = TrailerBrand
        fields = '__all__'


class TrailerTypeForm(ModelForm):
    class Meta:
        model = TrailerType
        fields = '__all__'
