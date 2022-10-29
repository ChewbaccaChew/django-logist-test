from django import forms
from django.contrib.auth import get_user_model

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

User = get_user_model()


class CarriersForm(forms.ModelForm):
    class Meta:
        model = Carrier
        fields = '__all__'


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'


class OrganizationalTypeForm(forms.ModelForm):
    class Meta:
        model = OrganizationalType
        fields = '__all__'


class CarrierTypeForm(forms.ModelForm):
    class Meta:
        model = CarrierType
        fields = '__all__'


class WheelFormulaForm(forms.ModelForm):
    class Meta:
        model = WheelFormula
        fields = '__all__'


class VehicleColourForm(forms.ModelForm):
    class Meta:
        model = VehicleColour
        fields = '__all__'


class VehicleTypeForm(forms.ModelForm):
    class Meta:
        model = VehicleType
        fields = '__all__'


class TrailerBrandForm(forms.ModelForm):
    class Meta:
        model = TrailerBrand
        fields = '__all__'


class TrailerTypeForm(forms.ModelForm):
    class Meta:
        model = TrailerType
        fields = '__all__'


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином "{username} не найден в системе')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data


class RegistrationForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердите пароль'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['address'].label = 'Адрес'
        self.fields['email'].label = 'Электронная почта'

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['com', 'net']:
            raise forms.ValidationError(
                f'Регистрация для домена {domain} невозможна'
            )
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Данный почтовый адрес уже зарегистрирован в системе'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Имя {username} занято'
            )
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'address', 'phone', 'email']
