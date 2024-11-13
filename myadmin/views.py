from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def Dashboard(request):
    imageslider = ImagesliderModel.objects.count()
    contex = {
        'imageslider': imageslider
    }
    return render(request, 'dashboard.html', contex)

def ImagSliderList(request):
    imagslider = ImagesliderModel.objects.all()
    contex = {
        'imagslider': imagslider
        }
    return render(request, 'imagsliderlist.html', contex)

def AddImagSlider(request):
    if request.method == 'GET':
        return render(request, 'addimagslider.html')
    if request.method == 'POST':
        imageslider = ImagesliderModel.objects.create(
            image = request.FILES['image'],
            title = request.POST['title'],
            desc = request.POST['desc'],
        )
        imageslider.save()
        return redirect('/myadmin/imagesliderlist/')