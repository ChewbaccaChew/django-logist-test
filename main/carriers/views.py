from django.shortcuts import render
from django.views import generic

from .models import Carrier


def index(request):
    carriers = Carrier.objects.all()
    return render(request, 'carriers/index.html', {'carriers': carriers})
