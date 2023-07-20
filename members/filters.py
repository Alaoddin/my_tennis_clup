from cProfile import label
from operator import contains
from pyexpat import model
from random import choices
import django_filters
from .models import *




# city choise
dzr_city=[
            ("مدينة ديرالزور","مدينة ديرالزور"),
            ("موحسن","موحسن"),
            ("ابوعمر","ابوعمر"),
            ("العبد","العبد"),
            ("البوليل","البوليل"),
            ("الطوب","الطوب"),
            ("الزباري","الزباري"),
            ("سعلو","سعلو"),
            ("مدينة الميادين","مدينة الميادين"),
            ("محكان","محكان"),
            ("القورية","القورية"),
            ("عشارة ","عشارة "),
            ("غريبه","غريبه"),
            ("تشرين","تشرين"),
            ("صبيخان","صبيخان"),
            ("دوير","دوير"),
        ("مدينة البوكمال","مدينة البوكمال"),
    ]


### start mabani filter
class MabaniFilter(django_filters.FilterSet):
    for_what =[("بيع","بيع"),("آجار","آجار"),(" رهن"," رهن")]  
    type =[("أرض","أرض"),("شقة","شقة"),("فيلا","فيلا"),("محل","محل")]
    city =django_filters.ChoiceFilter(label="المدينة :",choices=dzr_city)
    estate_type =django_filters.ChoiceFilter(choices=type,label="نوع العقار :")
    name =django_filters.ChoiceFilter(choices=for_what,label="نوع المعاملة: ")
    adress = django_filters.CharFilter(lookup_expr='icontains' ,label="العنوان :")
    class Meta:
        model = Mabani
        fields = ['name','estate_type','city','adress']
### end mabani filter
      
### start car filter
       
class CarFilter(django_filters.FilterSet):
    
    type =[
       ("الفاروميو","الفاروميو"),
        ("ام جي","ام جي"),
        ("ايسوزو","ايسوزو"),
        ("أوبل","أوبل"),
        ("أودي","أودي"),
        ("بايك","بايك"),
        ("بروتون","بروتون"),
        ("بريليانس","بريليانس"),
        ("بنتلي","بنتلي"),
        ("بورش","بورش"),
        ("بونتياك","بونتياك"),
        ("بي ام دبليو","بي ام دبليو"),
        ("بي واي دي","بي واي دي"),
        ("بيجو","بيجو"),
        ("تاتا","تاتا"),
        ("تويوتا","تويوتا"),
        ("تيسلا","تيسلا"),
        ("جاكوار","جاكوار"),
        ("جريت وول","جريت وول"),
        ("جي إم سي","جي إم سي"),
        ("جيب","جيب"),
        ("جيلي","جيلي"),
        ("جيه إيه سي","جيه إيه سي"),
        ("دايهاتسو","دايهاتسو"),
        ("دايو","دايو"),
        ("دودج","دودج"),
        ("دي اف ام","دي اف ام"),
        ("رولز رویس","رولز رویس"),
        ("رينو","رينو"),
        ("سانغ يونغ","سانغ يونغ"),
        ("سايبا","سايبا"),
        ("ستيروين","ستيروين"),
        ("سكودا","سكودا"),
        ("سوبارو","سوبارو"),
        ("سوزوكي","سوزوكي"),
        ("سيات","سيات"),
        ("شانجان","شانجان"),
        ("شيري","شيري"),
        ("شيفروليه","شيفروليه"),
        ("فوتون","فوتون"),
        ("فورد","فورد"),
        ("فولفو","فولفو"),
        ("فولكسفاغن","فولكسفاغن"),
        ("فيات","فيات"),
        ("فيراري","فيراري"),
        ("كرايسلر","كرايسلر"),
        ("كيا","كيا"),
        ("لادا","لادا"),
        ("لاند روفر","لاند روفر"),
        ("لكزس","لكزس"),
        ("ماروتي","ماروتي"),
        ("مازدا","مازدا"),
        ("مرسيدس بنز","مرسيدس بنز"),
        ("ميتسوبيشي","ميتسوبيشي"),
        ("ميني","ميني"),
        ("نيسان","نيسان"),
        ("هوندا","هوندا"),
        ("هيونداي","هيونداي"),
        
        
    ]
    
    car_year = django_filters.CharFilter(lookup_expr='icontains' ,label="سنة التصنيع :")
    price = django_filters.RangeFilter(label="السعر :")
    car_type =django_filters.ChoiceFilter(label="نوع السيارة :",choices=type)
    city =django_filters.ChoiceFilter(label="المدينة :",choices=dzr_city)
    class Meta:
        model = Car
        fields = ['city','car_type','car_year','price']
        
### end car filter  
     
### start phone filter
class PhoneFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الاسم :')
    screen  = django_filters.NumberFilter(label="حجم الشاشة :")
    memory   = django_filters.NumberFilter(label="الذاكرة:")
    ram     = django_filters.NumberFilter(label="الرام:" )
    price = django_filters.RangeFilter(label='السعر:')
    city =django_filters.ChoiceFilter(label="المدينة :",choices=dzr_city)
    class Meta:
        model=Phone
        fields=['name', 'city','price','screen','memory','ram']

### end phone filter

### start laptop filter
class LaptopFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label='الاسم :')
    city =django_filters.ChoiceFilter(label="المدينة :",choices=dzr_city)
    screen  = django_filters.NumberFilter(label="حجم الشاشة :")
    hard   = django_filters.NumberFilter(label="الهارد:")
    ram     = django_filters.NumberFilter(label="الرام:" )
    cpu = django_filters.CharFilter(lookup_expr='icontains',label='نوع المعالج :')
    price = django_filters.RangeFilter(label='السعر:')
    class Meta:
        model=Laptop
        fields=['name', 'city','screen','hard','ram','cpu','price' ]
### end laptop filter

####==================================###
class E_Filter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label="اسم القعطة :")
    price = django_filters.RangeFilter(label="السعر:")
    city =django_filters.ChoiceFilter(label="المدينة :",choices=dzr_city)
    class Meta:
        model=Electrical_tools
        fields=['name', 'city','price']
        
        
class HouseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label="نوع الأثاث:")
    price = django_filters.RangeFilter(label="السعر:")
    city =django_filters.ChoiceFilter(label="المدينة :",choices=dzr_city)
    class Meta:
        model=House_tools
        fields=['name', 'city','price']
        

class KitchenFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains',label="اسم القعطة :")
    price = django_filters.RangeFilter(label="السعر:")
    city =django_filters.ChoiceFilter(label="المدينة :",choices=dzr_city)
    class Meta:
        model=Kitchen_tools
        fields=['name', 'city','price']
        
   
   
class MotorBikeFilter(django_filters.FilterSet):
    motor_type = django_filters.CharFilter(lookup_expr='icontains',label="نوع الدراجة  :")
    year_made = django_filters.CharFilter(lookup_expr='icontains',label="سنة التصنيع :")
    price = django_filters.RangeFilter(label="السعر:")
    city =django_filters.ChoiceFilter(label="المدينة :",choices=dzr_city)
    class Meta:
        model=MotorBike
        fields=['motor_type','year_made', 'city','price']
             
