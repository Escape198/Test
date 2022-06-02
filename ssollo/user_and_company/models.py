from django.db import models
from datetime import date


class Person(models.Model):

    position_list=[
        (0 ,'Admin'),
        (1, 'Employee'),
        (2, 'Client')
    ]

    Company=models.ForeignKey('Company', verbose_name='Company', on_delete=models.PROTECT, blank=True, null=True)
    Name=models.CharField('Name', max_length=50)
    Fname=models.CharField('Surname', max_length=50)
    Date=models.DateField('Date_of_birth', blank=True, null=True)
    Phone=models.CharField('Phone', max_length=12)
    Email=models.EmailField('Email')
    Passport=models.CharField('Passport', max_length=50, blank=True, null=True)
    Position=models.IntegerField('Position', blank=True, null=True, choices=position_list, default=0)
    Comment=models.TextField('Comments', blank=True, null=True)
    NumVU=models.CharField('NumVU', max_length=50, blank=True, null=True)
    Password=models.CharField('Password', max_length=150, blank=True, null=True)
    DateDel=models.DateField('Delete_date', blank=True, null=True)
    CategoryVU = models.JSONField('Categories', blank=True, null=True)

    def __str__(self):
        return self.Name + self.Fname + self.Phone

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

    def add_client(client, request, data):
        client.Name = request.POST.get('Name')
        client.Fname = request.POST.get('Fname')
        client.Email = request.POST.get('Email')
        client.Phone = request.POST.get('Phone')
        client.Date = request.POST.get('Date')
        client.Passport = request.POST.get('Passport')
        client.NumVU = request.POST.get('NumVU')
        client.Position = 2
        client.CategoryVU = data
        client.save()
        return client

    def update_client(client, request, pk, data):
        client = Person.objects.get(id=pk)
        client.Name = request.POST.get('Name')
        client.Fname = request.POST.get('Fname')
        client.Email = request.POST.get('Email')
        client.Phone = request.POST.get('Phone')
        client.Date = request.POST.get('Date')
        client.Passport = request.POST.get('Passport')
        client.NumVU = request.POST.get('NumVU')
        client.CategoryVU = data
        client.save()
        return client

    def delete_user(pk):
        user = Person.objects.get(id=pk)
        user.DateDel = date.today()
        user.save()
        return True

    def add_admin(admin, request):
        admin.Name = request.POST.get('Name')
        admin.Fname = request.POST.get('Fname')
        admin.Email = request.POST.get('Email')
        admin.Phone = request.POST.get('Phone')
        admin.Comment = request.POST.get('Comment')
        admin.Position = 0
        admin.save()
        return admin

    def update_admin(admin, request, pk):
        admin = Person.objects.get(id=pk)
        admin.Name = request.POST.get('Name')
        admin.Fname = request.POST.get('Fname')
        admin.Email = request.POST.get('Email')
        admin.Phone = request.POST.get('Phone')
        admin.Comment = request.POST.get('Comment')
        admin.save()
        return admin

    def add_employee(employee, request, pk):
        employee.Name = request.POST.get('Name')
        employee.Fname = request.POST.get('Fname')
        employee.Email = request.POST.get('Email')
        employee.Phone = request.POST.get('Phone')
        employee.Comment = request.POST.get('Comment')
        employee.Company_id = pk
        employee.Position = 1
        employee.save()
        return employee

    def update_employee(employee, request, pk):
        employee = Person.objects.get(id=pk)
        employee.Name = request.POST.get('Name')
        employee.Fname = request.POST.get('Fname')
        employee.Email = request.POST.get('Email')
        employee.Phone = request.POST.get('Phone')
        employee.Comment = request.POST.get('Comment')
        employee.save()
        return employee


class Company(models.Model):
    Name=models.CharField('Name', max_length=50)
    Phone=models.CharField('Phone', max_length=12)
    Email=models.EmailField('Email')
    Note=models.TextField('Note', blank=True, null=True)
    DateDel=models.DateField('Delete_date', blank=True, null=True)
    ContactFIO=models.CharField('Contact',  max_length=150, blank=True)
    ContactPhone=models.CharField('Phone',  max_length=12)
    ContactEmail=models.EmailField('Email')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name='Company'
        verbose_name_plural='Companies'

    def add_company(company, request):
        company.Name = request.POST.get('Name')
        company.Email = request.POST.get('Email')
        company.Phone = request.POST.get('Phone')
        company.Note = request.POST.get('Note')
        company.ContactFIO = request.POST.get('ContactFIO')
        company.ContactEmail = request.POST.get('ContactEmail')
        company.ContactPhone = request.POST.get('ContactPhone')
        company.save()
        return company

    def update_company(company, request, pk):
        company = Company.objects.get(id=pk)
        company.Name = request.POST.get('Name')
        company.Email = request.POST.get('Email')
        company.Phone = request.POST.get('Phone')
        company.Note = request.POST.get('Note')
        company.ContactFIO = request.POST.get('ContactFIO')
        company.ContactEmail = request.POST.get('ContactEmail')
        company.ContactPhone = request.POST.get('ContactPhone')
        company.save()
        return company

    def delete_company(pk):
        company = Company.objects.get(id=pk)
        company.DateDel = date.today()
        company.save()
        return True
