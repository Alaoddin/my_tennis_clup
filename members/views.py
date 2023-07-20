
import re
from typing import Any, Dict
from urllib import request
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.template import loader
from .models import *
from .form import EstateForm
import csv
from .filters import *
from django.views.generic import ListView,DeleteView
from hitcount.views import HitCountDetailView
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def estates(request):
    estates = Mabani.objects.all()
    myfilter = MabaniFilter(request.GET,queryset=estates)
    estates = myfilter.qs
    template2 = loader.get_template('estate.html')
    context = {
      'estates': estates,
      'myfilter':myfilter
      
    }
    return HttpResponse(template2.render(context,request))


#  to export data 
def export_csv(request):
      response = HttpResponse(content_type='text/csv')
      response['Content-Disposition'] = 'attachment; filename="products.csv"'

      writer = csv.writer(response)
      writer.writerow(['Name', 'Price', 'Description'])

      products = Mabani.objects.all()
      for product in products:
          writer.writerow([product.name, product.prise, product.Description])
          
      response.encoding("windos-1252")

      return response
    



# =========
def cars(request):
    cars =Car.objects.all()
    
    myfilter = CarFilter(request.GET,queryset=cars)
    cars=myfilter.qs
    template2 = loader.get_template('cars.html')
    context = {
      'cars': cars,
      'myfilter':myfilter,
    }
    return HttpResponse(template2.render(context,request))
 
 # =========
def motorbike(request):
   motor =MotorBike.objects.all()
   myfilter =MotorBikeFilter(request.GET,queryset=motor)
   motor =myfilter.qs
   template2 = loader.get_template('motor.html')
   context = {
    'motor': motor,
    'myfilter':myfilter
  }
   return HttpResponse(template2.render(context,request))
 # =========
def car_de(request,id):
  
  
  car_de = Car.objects.get(id=id)
  template = loader.get_template('car_details.html')
  context = {
    'car_de': car_de,
  }
  return HttpResponse(template.render(context, request))

# =========

def motor_de(request,id):
  
 
  
  motor_de = MotorBike.objects.get(id=id)
  template = loader.get_template('motor_details.html')
  context = {
    'motor_de': motor_de,
  }
  return HttpResponse(template.render(context, request))

# =========

def kitchen(request):
  
   kitchen =Kitchen_tools.objects.all()
   myfilter = KitchenFilter(request.GET,queryset=kitchen)
   kitchen=myfilter.qs
   template2 = loader.get_template('kitchen.html')
   context = {
    'kitchen': kitchen,
    'myfilter':myfilter,
  }
   return HttpResponse(template2.render(context,request))


class PhoneList(ListView):

  queryset = Phone.objects.all()
  context_object_name="phones"
  def get_queryset(self):
    queryset = super().get_queryset()
    self.filterset = PhoneFilter(self.request.GET,queryset=queryset)
    return self.filterset.qs
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['filter']=self.filterset.form
    return context
  



class LaptopList(ListView):
  
  queryset = Laptop.objects.all()
  context_object_name="laptops"
  def get_queryset(self):
    queryset = super().get_queryset()
    self.filterset = LaptopFilter(self.request.GET,queryset=queryset)
    return self.filterset.qs
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['filter']=self.filterset.form
    return context

# أدوات المنزل
class Electrical_toolsList(ListView):
  
  queryset = Electrical_tools.objects.all()
  context_object_name="Electrical_tools"
  def get_queryset(self):
    queryset = super().get_queryset()
    self.filterset = E_Filter(self.request.GET,queryset=queryset)
    return self.filterset.qs
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['filter']=self.filterset.form
    return context
  

  
class HouseList(ListView):
  
  queryset = House_tools.objects.all()
  context_object_name="house"
  def get_queryset(self):
    queryset = super().get_queryset()
    self.filterset = HouseFilter(self.request.GET,queryset=queryset)
    return self.filterset.qs
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['filter']=self.filterset.form
    return context
  
  
  
# قسم خاص بعدد  المشاهدات 

class MabaniDetailView(HitCountDetailView):
  model = Mabani
  context_object_name = 'mabani'
  template_name = "mabani_detail.html"
  count_hit = True



def Mabani_detail(request,id):
     mabani = Mabani.objects.get(pk=id)
     return render(request, 'mabani_detail.html', {'mabani': mabani, 'hit_count': mabani.hit_count.hits})