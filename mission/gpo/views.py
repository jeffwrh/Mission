from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from .models import *
# from .forms import *

def accueil(request):
    mission = Mission.objects.all()
    return render(request, 'accueil.html', {'mission': mission})
