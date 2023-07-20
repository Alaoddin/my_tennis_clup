from django.urls import path

from .views import *
from . import views
urlpatterns = [
    
    path('',index,name ='index'),
    path('estate/',estates,name ='estates'),
    path('mabani/<int:pk>/', views.MabaniDetailView.as_view(), name='mabani_detail'),
    # path('estate/estate_details/<int:id>',estate_de,name ='estate_de'),
    path('cars',cars,name ='cars'),
    path('cars/car_details/<int:id>',car_de,name ='car_de'),
    path('motor',motorbike,name ='motorBike'),
    path('motor/motor_details/<int:id>',motor_de,name ='motor_de'),
    path('kitchen',kitchen,name ='kitchen'),
    path('phone',views.PhoneList.as_view(),name ='phone'),
    path('laptop',views.LaptopList.as_view(),name ='laptop'),
    path('electrical',views.Electrical_toolsList.as_view(),name ='electrical'),
    path('house',views.HouseList.as_view(),name ='house'),
    
    path('export-csv/', export_csv, name='export-csv'),
    
]

