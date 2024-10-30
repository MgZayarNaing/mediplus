from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    imageslider = ImagesliderModel.objects.all().order_by('-id')
    emergencycases = EmergencyCasesModel.objects.all().order_by('-id')[:2]
    openhours = OpeningHoursModel.objects.all().order_by('-id')[:2]
    exp = ExpModel.objects.all().order_by('-id')[:4]

    contex  = {
    'imageslider':imageslider,
    'emergencycases':emergencycases,
    'openhours':openhours,
    'exp':exp,
    }
    return render(request,'index.html',contex )