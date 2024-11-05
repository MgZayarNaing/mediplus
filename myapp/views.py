from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    imageslider = ImagesliderModel.objects.all().order_by('-id')
    emergencycases = EmergencyCasesModel.objects.all().order_by('-id')[:2]
    openhours = OpeningHoursModel.objects.all().order_by('-id')[:2]
    exp = ExpModel.objects.all().order_by('-id')[:4]
    feature = FeatureModel.objects.all().order_by('-id')[:3]
    whoweare = WhoWeAreModel.objects.all().order_by('-id')[:1]
    whowearelist = WhoWeAreListModel.objects.all().order_by('-id')[:4]

    contex  = {
    'imageslider':imageslider,
    'emergencycases':emergencycases,
    'openhours':openhours,
    'exp':exp,
    'feature':feature,
    'whoweare':whoweare,
    'whowearelist':whowearelist,
    }
    return render(request,'index.html',contex )