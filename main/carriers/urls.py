# -*- coding: utf-8 -*-

from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'carriers'

urlpatterns = [
    path('add-trailer-type/', views.CreateTrailerTypeView.as_view(), name='add_trailer_type'),
    path('add-trailer-brand/', views.CreateTrailerBrandView.as_view(), name='add_trailer_brand'),
    path('add-vehicle-type/', views.CreateVehicleTypeView.as_view(), name='add_vehicle_type'),
    path('add-vehicle-colour/', views.CreateVehicleColourView.as_view(), name='add_vehicle_colour'),
    path('add-wheel-formula/', views.CreateWheelFormulaView.as_view(), name='add_wheel_formula'),
    path('add-carrier-type/', views.CreateCarrierTypeView.as_view(), name='add_carrier_type'),
    path('add-organizational-type/', views.CreateOrganizationalTypeView.as_view(), name='add_organizational_type'),
    path('add-driver/', views.CreateDriverView.as_view(), name='add_driver'),
    path('add-vehicle/', views.CreateVehicleView.as_view(), name='add_vehicle'),
    path('add-carrier/', views.CreateCarrierView.as_view(), name='add_carrier'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('', views.index, name='index'),
]

# urlpatterns = [
#     # /carriers/
#     path('', views.CarrierListView.as_view(), name='index'),
#     # /carriers/5/
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     # /carriers/5/results/
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     # /carriers/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
