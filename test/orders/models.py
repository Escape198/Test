#import datetime
from datetime import date, timedelta
import decimal

from django.db import models
from django.db.models.fields import DecimalField

from cars.models import Car
from feedback_and_comments.models import FeedBackAndComment
from user_and_company.models import Person


class Contract(models.Model):
    Client=models.ForeignKey('user_and_company.Person', verbose_name='Клиент', on_delete=models.PROTECT, blank=True, null=True)
    Car=models.ForeignKey('cars.Car', verbose_name='Car', on_delete=models.PROTECT, blank=True, null=True, related_name='car')
    DateStartContract=models.DateField('Start date', blank=True, null=True)
    DateEndContract=models.DateField('End Date', blank=True, null=True)
    Driver=models.BooleanField('Need a driver', blank=True, null=True)
    Note=models.TextField('Note', blank=True, null=True)
    Status=models.IntegerField('Order status', blank=True, null=True)
    Comission=models.DecimalField('Commission', max_digits=10, decimal_places=2, blank=True, null=True )
    Cost=models.IntegerField('Cost', blank=True, null=True )
    DateDel=models.DateField('Delete date', blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name='Order'
        verbose_name_plural='Orders'
        ordering = ['-id']

    def add_order(order, request):
        car = Car.objects.get(id=int(request.POST.get('Car')))
        end = datetime.datetime.strptime(request.POST.get('DateEndContract'), '%Y-%m-%d')
        start = datetime.datetime.strptime(request.POST.get('DateStartContract'), '%Y-%m-%d')
        if (end == start):
            rez = 1
        else:
            rez = (end-start).days
        cost =  rez * car.Price
        order.Client_id = request.POST.get('Client')
        order.Car_id = request.POST.get('Car')
        order.DateStartContract = request.POST.get('DateStartContract')
        order.DateEndContract = request.POST.get('DateEndContract')
        order.Driver = request.POST.get('Driver')
        order.Note = request.POST.get('Note')
        order.Status = 0
        if (int(request.POST.get('Driver')) == 1):
            driver = 1500
        else:
            driver = 0
        order.Cost = cost + driver
        car_per = car.Percent
        car_fix = car.FixedRate + decimal.Decimal(driver)
        per1 = car_per * decimal.Decimal(0.01)
        per2 = round((per1 * decimal.Decimal(cost)) + car_fix , 2)
        order.Comission = per2
        order.save()
        return order

    def add_order_client(order, request, pk):
        car = Car.objects.get(id=pk)
        end = datetime.datetime.strptime(request.POST.get('DateEndContract'), '%Y-%m-%d')
        start = datetime.datetime.strptime(request.POST.get('DateStartContract'), '%Y-%m-%d')
        if (end == start):
            rez = 1
        else:
            rez = (end-start).days
        if (request.POST.get("Driver") == 'on'):
            order.Driver = True
            driver = 1500
        else:
            order.Driver = False
            driver = 0
        order.Client_id = 10
        order.Car_id = car.id
        order.DateStartContract = request.POST.get('DateStartContract')
        order.DateEndContract = request.POST.get('DateEndContract')
        cost =  rez * car.Price
        order.Cost = cost + driver
        car_per = car.Percent
        car_fix = car.FixedRate + decimal.Decimal(driver)
        per1 = car_per * decimal.Decimal(0.01)
        per2 = round((per1 * decimal.Decimal(cost)) + car_fix , 2)
        order.Comission = per2
        order.Status = 0
        order.save()
        return order

    def update_order(order, request, pk):
        order = Contract.objects.get(id=pk)
        car = Car.objects.get(id=int(request.POST.get('Car')))
        end = datetime.datetime.strptime(request.POST.get('DateEndContract'), '%Y-%m-%d')
        start = datetime.datetime.strptime(request.POST.get('DateStartContract'), '%Y-%m-%d')
        rez = (end-start).days
        order.Car_id = request.POST.get('Car')
        order.DateStartContract = request.POST.get('DateStartContract')
        order.DateEndContract = request.POST.get('DateEndContract')
        order.Driver = request.POST.get('Driver')
        order.Note = request.POST.get('Note')

        if (request.POST.get("Driver") == "1"):
            order.Driver = True
            driver = 1500
        else:
            order.Driver = False
            driver = 0
        cost =  rez * car.Price
        order.Cost = cost + driver
        car_per = car.Percent
        car_fix = car.FixedRate + decimal.Decimal(driver)
        per1 = car_per * decimal.Decimal(0.01)
        per2 = round((per1 * decimal.Decimal(cost)) + car_fix , 2)
        order.Comission = per2
        order.save()
        return order

    def end_order(pk):
        order = Contract.objects.get(id=pk)
        order.Status = 2
        order.save()
        return order

    def cancel_order(pk):
        order = Contract.objects.get(id=pk)
        order.Status = 1
        order.save()
        return order


class Message(models.Model):
    Contract = models.ForeignKey('Contract', verbose_name='Order', on_delete=models.PROTECT, blank=True, null=True)
    From = models.ForeignKey('user_and_company.Person', verbose_name='Send', on_delete=models.PROTECT, blank=True, null=True)
    Message = models.TextField('Message', blank=True, null=True)
    Date=models.DateTimeField('Date', blank=True, null=True)
    Status=models.BooleanField('Status', blank=True, null=True)

    def __str__(self):
        return self.Contract

    class Meta:
        verbose_name='Message'
        verbose_name_plural='Messages'

    def add_message(id, message):
        person_from = 2
        mes = Message.objects.create(Contract_id=id,Date = datetime.datetime.now(), Message = message , From_id = person_from)
        mes.save()
        return mes
