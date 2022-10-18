# -*- coding: utf-8 -*-

from django.urls import path, re_path

from . import views

app_name = 'carriers'

urlpatterns = [
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
