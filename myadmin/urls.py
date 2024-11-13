from django.urls import path
from . import views
# from .views import *
urlpatterns = [
    # path('dashboard/', Dashboard, name='Dashboard'),
    path('dashboard/', views.Dashboard, name='Dashboard'),
    path('imagesliderlist/', views.ImagSliderList, name='ImagesliderList'),
    path('imageslidercreate/', views.AddImagSlider, name='AddImagSlider'),
]
