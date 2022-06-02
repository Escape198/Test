from datetime import date
from django.db import models


class Car(models.Model):
    transmission_list=[
        (0 ,'Manual'),
        (1, 'Auto')
    ]
    engine_list=[
        (0 ,'Petrol '),
        (1, 'Diesel')
    ]
    car_type_list=[
        (0 ,'Sedan'),
        (1, 'Crossover'),
        (2 ,'Universal'),
        (3 ,'Hatchback'),
        (4 ,'Coupe'),
        (5 ,'Micro')
    ]
    drive_list=[
        (0 ,'Full'),
        (1, 'Back'),
        (2 ,'Front')
    ]
    wheel_drive_list=[
        (0 ,'Right'),
        (1, 'Left')
    ]
    CompanyID=models.ForeignKey( 'user_and_company.Company', verbose_name='ID Company', on_delete=models.PROTECT, blank=True)
    Location=models.CharField('Location', max_length=250, blank=True, null=True)
    Photos = models.JSONField('')
    RentCondition=models.TextField('RentCondition', blank=True, null=True)
    Header=models.CharField('Header', max_length=150, blank=True, null=True)
    Driver=models.BooleanField('Driver', blank=True, null=True)
    Status=models.BooleanField('Status', blank=True, null=True)
    CategoryID=models.ForeignKey('Category', verbose_name='Category', on_delete=models.PROTECT)
    CategoryVU=models.CharField('CategoryVUID', max_length=250, blank=True, null=True)
    DateDel=models.DateField('Delete date', blank=True, null=True)
    FixedRate=models.DecimalField('FixedRate', max_digits=5, decimal_places=2, blank=True, null=True )
    Percent=models.DecimalField('Percent', max_digits=5, decimal_places=2, blank=True, null=True )

    Brand_and_name=models.CharField('Brand_and_name',max_length=150, blank=True, null=True)
    Transmission=models.IntegerField('Transmission',blank=True, null=True, choices=transmission_list, default=0)
    Engine=models.IntegerField('Engine', blank=True, null=True, choices=engine_list, default=0)
    Car_type=models.IntegerField('Car_type', blank=True, null=True, choices=car_type_list, default=0)
    Drive=models.IntegerField('Drive ', blank=True, null=True, choices=drive_list, default=0)
    Wheel_drive=models.IntegerField('Wheel_drive', blank=True, null=True, choices=wheel_drive_list, default=0)
    Year=models.IntegerField('Year', blank=True, null=True)
    Power=models.IntegerField('Power', blank=True, null=True)
    Price=models.IntegerField('Cost', blank=True, null=True)

    def __str__(self):
        return self.Brand_and_name

    class Meta:
        verbose_name='Car'
        verbose_name_plural='Cars'


    def add_car(car, request, json):
        car.Photos = json
        car.Header = request.POST.get('Header')
        car.CategoryID_id =request.POST.get('CategoryID')
        car.CompanyID_id =request.POST.get('CompanyID')
        car.Brand_and_name = request.POST.get('Brand_and_name')
        car.Car_type = request.POST.get('Car_type')
        car.Engine = request.POST.get('Engine')
        car.Transmission = request.POST.get('Transmission')
        car.Drive = request.POST.get('Drive')
        car.Wheel_drive = request.POST.get('Wheel_drive')
        car.Year = request.POST.get('Year')
        car.Driver = request.POST.get('Driver')
        car.Power = request.POST.get('Power')
        car.CategoryVUID = request.POST.get('CategoryVUID')
        car.Price = request.POST.get('Price')
        car.FixedRate = request.POST.get('FixedRate')
        car.Percent = request.POST.get('Percent')
        car.Location = request.POST.get('Location')
        car.RentCondition = request.POST.get('RentCondition')
        car.save()
        return car

    def update_car(car, request, pk):
        car = Car.objects.get(id=pk)
        car.Header = request.POST.get('Header')
        car.CategoryID_id =request.POST.get('CategoryID')
        car.CompanyID_id =request.POST.get('CompanyID')
        car.Brand_and_name = request.POST.get('Brand_and_name')
        car.Car_type = request.POST.get('Car_type')
        car.Engine = request.POST.get('Engine')
        car.Transmission = request.POST.get('Transmission')
        car.Drive = request.POST.get('Drive')
        car.Wheel_drive = request.POST.get('Wheel_drive')
        car.Year = request.POST.get('Year')
        car.Driver = request.POST.get('Driver')
        car.Power = request.POST.get('Power')
        car.CategoryVUID = request.POST.get('CategoryVUID')
        car.Price = request.POST.get('Price')
        car.FixedRate = request.POST.get('FixedRate')
        car.Percent = request.POST.get('Percent')
        car.Location = request.POST.get('Location')
        car.RentCondition = request.POST.get('RentCondition')
        car.save()
        return car

    def delete_car(pk):
        car = Car.objects.get(id=pk)
        car.DateDel = date.today()
        car.save()
        return True

    def hidden_car(pk):
        car = Car.objects.get(id=pk)
        car.Status = 1
        car.save()
        return car

    def visible_car(pk):
        car = Car.objects.get(id=pk)
        car.Status = 0
        car.save()
        return car


class Category(models.Model):
    NameCat=models.CharField('Name', max_length=100)
    Icon=models.ImageField(verbose_name='Icon', upload_to='img_category')
    DateDel=models.DateField('Delete date')
    Percent=models.DecimalField('Percent', max_digits=5, decimal_places=2 )
    FixedRate=models.DecimalField('FixedRate', max_digits=5, decimal_places=2 )

    def __str__(self):
        return self.NameCat

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
