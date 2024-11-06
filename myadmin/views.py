from django.shortcuts import render
from myapp.models import *
# Create your views here.

def Dashboard(request):
    imageslider = ImagesliderModel.objects.all()
    contex = {
        'imageslider': imageslider
    }
    return render(request, 'dashboard.html', contex)