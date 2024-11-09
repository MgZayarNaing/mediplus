from django.shortcuts import render
from myapp.models import *
# Create your views here.

def Dashboard(request):
    imageslider = ImagesliderModel.objects.count()
    contex = {
        'imageslider': imageslider
    }
    return render(request, 'dashboard.html', contex)