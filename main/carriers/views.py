from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Carrier
from .forms import (
    CarriersForm,
    VehicleForm,
    DriverForm,
    OrganizationalTypeForm,
    CarrierTypeForm,
    WheelFormulaForm,
    VehicleColourForm,
    VehicleTypeForm,
    TrailerBrandForm,
    TrailerTypeForm,
)


def index(request):
    carriers = Carrier.objects.all()
    return render(request, 'carriers/index.html', {'carriers': carriers})


class CreateCarrierView(CreateView):
    template_name = 'carriers/create_carrier.html'
    form_class = CarriersForm
    success_url = 'http://127.0.0.1:8000/'  # разобраться с адресом перенаправления

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['carriers'] = Carrier.objects.all()
    #     return context


class CreateVehicleView(CreateView):
    template_name = 'carriers/create_vehicle.html'
    form_class = VehicleForm
    success_url = 'http://127.0.0.1:8000/'


class CreateDriverView(CreateView):
    template_name = 'carriers/create_driver.html'
    form_class = DriverForm
    success_url = 'http://127.0.0.1:8000/'


class CreateOrganizationalTypeView(CreateView):
    template_name = 'carriers/create_organizational_type.html'
    form_class = OrganizationalTypeForm
    success_url = 'http://127.0.0.1:8000/'


class CreateCarrierTypeView(CreateView):
    template_name = 'carriers/create_carrier_type.html'
    form_class = CarrierTypeForm
    success_url = 'http://127.0.0.1:8000/'


class CreateWheelFormulaView(CreateView):
    template_name = 'carriers/create_wheel_formula.html'
    form_class = WheelFormulaForm
    success_url = 'http://127.0.0.1:8000/'


class CreateVehicleColourView(CreateView):
    template_name = 'carriers/create_vehicle_colour.html'
    form_class = VehicleColourForm
    success_url = 'http://127.0.0.1:8000/'


class CreateVehicleTypeView(CreateView):
    template_name = 'carriers/create_vehicle_type.html'
    form_class = VehicleTypeForm
    success_url = 'http://127.0.0.1:8000/'


class CreateTrailerBrandView(CreateView):
    template_name = 'carriers/create_trailer_brand.html'
    form_class = TrailerBrandForm
    success_url = 'http://127.0.0.1:8000/'


class CreateTrailerTypeView(CreateView):
    template_name = 'carriers/create_trailer_type.html'
    form_class = TrailerTypeForm
    success_url = 'http://127.0.0.1:8000/'
