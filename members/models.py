from django.db import models
from hitcount.models import HitCountMixin, HitCount
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
# هنا تصميم قاعدة بيانات العقارات
class Mabani(models.Model,HitCountMixin):
    
    for_what =[("بيع","بيع"),("آجار","آجار"),(" رهن"," رهن")]  
    type =[("أرض","أرض"),("شقة","شقة"),("فيلا","فيلا"),("محل","محل")]
    name = models.CharField(max_length=255,choices=for_what)
    # buy = models.CharField(max_length=255)
    prise =models.IntegerField(null=True)
    post_date =models.DateField(null=True)
    adress = models.CharField(max_length=255,null=True)
    estate_type = models.CharField(max_length=255,null=True,choices=type)
    estate_size = models.IntegerField(null=True)
    city = models.CharField(max_length=255,null=True,choices=dzr_city)
    neighborhood = models.CharField(max_length=255,null=True)
    Description = models.CharField(max_length=255,null=True)
    # contact_number = models.CharField(max_length=10 , null=False)
    image_one =models.ImageField(upload_to="photos",null=True,blank=True)
    image_tow =models.ImageField(upload_to="photos",null=True,blank=True)
    image_three =models.ImageField(upload_to="photos",null=True,blank=True)
    image_fore =models.ImageField(upload_to="photos",null=True,blank=True)
    hit_count_generic = models.OneToOneField(HitCount, related_name='hit_count_generic', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.estate_type }'
    
    # car databases
# هنا تصميم قاعدة بيانات السيارات
class Car(models.Model):
    
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

    car_type = models.CharField(max_length=100 , null=False,choices=type)
    price =models.IntegerField(null=True)
    car_year = models.CharField(max_length=4 , null=False)
    Description = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True,choices=dzr_city)
    neighborhood = models.CharField(max_length=255,null=True)
    phone_owner = models.CharField(max_length=10 , null=False)
    image_one =models.ImageField(upload_to="carphoto",null=True,blank=True)
    image_tow =models.ImageField(upload_to="carphoto",null=True,blank=True)
    image_three =models.ImageField(upload_to="carphoto",null=True,blank=True)
    image_fore =models.ImageField(upload_to="carphoto",null=True,blank=True)
    def __str__(self):
        return f'{self.car_type}'
    
    # 
# الدراجات النارية
class MotorBike(models.Model):
    motor_type=models.CharField(max_length=100 , null=False)
    year_made = models.CharField(max_length=4 , null=False)
    Description = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True,choices=dzr_city)
    price =models.IntegerField(null=True)
    neighborhood = models.CharField(max_length=255,null=True)
    phone_owner = models.CharField(max_length=10 , null=False)
    image_one =models.ImageField(upload_to="motorphoto",null=True,blank=True)
    image_tow =models.ImageField(upload_to="motorphoto",null=True,blank=True)
    image_three =models.ImageField(upload_to="motorphoto",null=True,blank=True)
    image_fore =models.ImageField(upload_to="motorphoto",null=True,blank=True)
    def __str__(self):
        return f'{self.motor_type}'
    
# أدوات المطبخ
class Kitchen_tools(models.Model):
    name = models.CharField(max_length=255,null=True)
    Description = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True,choices=dzr_city)
    price =models.IntegerField(null=True)
    neighborhood = models.CharField(max_length=255,null=True)
    phone_owner = models.CharField(max_length=10 , null=False)
    image_one =models.ImageField(upload_to="kitchenphoto",null=True,blank=True)
    image_tow =models.ImageField(upload_to="kitchenphoto",null=True,blank=True)
    def __str__(self):
        return f'{self.name}'


# الادوات الكهربائية
class Electrical_tools(models.Model):
    name = models.CharField(max_length=255,null=True)
    Description = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True,choices=dzr_city)
    price =models.IntegerField(null=True)
    neighborhood = models.CharField(max_length=255,null=True)
    phone_owner = models.CharField(max_length=10 , null=False)
    image_one =models.ImageField(upload_to="kitphoto",null=True,blank=True)
    image_tow =models.ImageField(upload_to="kitphoto",null=True,blank=True)
    def __str__(self):
        return f'{self.name}'
    


class House_tools(models.Model):
    name = models.CharField(max_length=255,null=True)
    Description = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True,choices=dzr_city)
    price =models.IntegerField(null=True)
    neighborhood = models.CharField(max_length=255,null=True)
    phone_owner = models.CharField(max_length=10 , null=False)
    image_one =models.ImageField(upload_to="house",null=True,blank=True)
    image_tow =models.ImageField(upload_to="house",null=True,blank=True)
    image_three =models.ImageField(upload_to="house",null=True,blank=True)
    image_fore =models.ImageField(upload_to="house",null=True,blank=True)
    def __str__(self):
        return f'{self.name}'

class Phone(models.Model):
    name = models.CharField(max_length=255,null=True)
    Description = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True,choices=dzr_city)
    neighborhood = models.CharField(max_length=255,null=True)
    screen= models.IntegerField(null=True)
    memory= models.IntegerField(null=True)
    ram= models.IntegerField(null=True)
    main_camera = models.IntegerField(null=True)
    selfie_camera = models.IntegerField(null=True)
    cpu = models.CharField(max_length=255,null=True)
    battery=models.IntegerField(null=True)
    price =models.IntegerField(null=True)
    phone_owner = models.CharField(max_length=10 , null=False)
    image_one =models.ImageField(upload_to="house",null=True,blank=True)
    image_tow =models.ImageField(upload_to="house",null=True,blank=True)
    image_three =models.ImageField(upload_to="house",null=True,blank=True)
    image_fore =models.ImageField(upload_to="house",null=True,blank=True)
    def __str__(self):
        return f'{self.name}'



class Laptop(models.Model):
    name = models.CharField(max_length=255,null=True)
    Description = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True,choices=dzr_city)
    neighborhood = models.CharField(max_length=255,null=True)
    screen= models.IntegerField(null=True)
    hard= models.IntegerField(null=True)
    ram= models.IntegerField(null=True)
    cpu = models.CharField(max_length=255,null=True)
    battery=models.IntegerField(null=True)
    price =models.IntegerField(null=True)
    phone_owner = models.CharField(max_length=10 , null=False)
    image_one =models.ImageField(upload_to="house",null=True,blank=True)
    image_tow =models.ImageField(upload_to="house",null=True,blank=True)
    image_three =models.ImageField(upload_to="house",null=True,blank=True)
    image_fore =models.ImageField(upload_to="house",null=True,blank=True)
    def __str__(self):
        return f'{self.name}'