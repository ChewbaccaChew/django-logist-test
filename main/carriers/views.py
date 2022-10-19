from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Carrier
from .forms import CarriersForm


def index(request):
    carriers = Carrier.objects.all()
    return render(request, 'carriers/index.html', {'carriers': carriers})


class CarriersCreateView(CreateView):
    template_name = 'carriers/create.html'
    form_class = CarriersForm
    success_url = 'http://127.0.0.1:8000/'  # разобраться с адресом перенаправления

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['carriers'] = Carrier.objects.all()
    #     return context
