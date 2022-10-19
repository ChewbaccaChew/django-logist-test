from django.forms import ModelForm

from .models import Carrier


class CarriersForm(ModelForm):
    class Meta:
        model = Carrier
        fields = '__all__'
