from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    imageslider = ImagesliderModel.objects.all().order_by('-id')
    emergencycases = EmergencyCasesModel.objects.all().order_by('-id')[:2]
    openhours = OpeningHoursModel.objects.all().order_by('-id')[:2]

    contex  = {
    'imageslider':imageslider,
    'emergencycases':emergencycases,
    'openhours':openhours,
    }
    return render(request,'index.html',contex )