from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Carrier


class CarrierListView(generic.ListView):

    template_name = 'carriers/index.html'
    context_object_name = 'question_list'
