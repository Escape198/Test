from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.forms import forms
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator

from user_and_company.forms import AdminForm, ClientForm, CompanyForm
from .models import Company, Person
from cars.models import Car, Category
from orders.models import Contract

import json


class Show_clients_list(ListView):
    model = Person
    template_name = 'user_and_company/admin_clients.html'
    context_object_name = 'clientget'
    queryset = Person.objects.filter(DateDel = None, Position =2)


class Show_client(DetailView):
    model = Person
    template_name = 'user_and_company/admin_info_client.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        cl = Person.objects.get(pk=self.kwargs['pk'])
        c = json.loads(cl.CategoryVU)

        ctx = super(Show_client, self).get_context_data(**kwargs)
        ctx['cats'] = c
        return ctx


class Add_client(CreateView):
    form_class = ClientForm
    template_name = 'user_and_company/admin_add_client.html'

    def post(self, request):
        lis = request.POST.getlist('CategoryVU')
        res = dict((i, lis.count(i)) for i in lis)
        data = json.dumps(res)
        form = ClientForm(request.POST)
        if (form.is_valid):
            cl = Person()
            cl= Person.add_client(cl, request, data)
        return redirect('admin_clients')


class Update_client(UpdateView):
    model = Person
    form_class = ClientForm
    template_name = 'user_and_company/admin_update_client.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        cl = Person.objects.get(pk=self.kwargs['pk'])
        c = json.loads(cl.CategoryVU)

        ctx = super(Update_client, self).get_context_data(**kwargs)
        ctx['cats'] = c
        return ctx

    def post(self, request, pk):
        lis = request.POST.getlist('CategoryVU')
        res = dict((i, lis.count(i)) for i in lis)
        data = json.dumps(res)
        form = ClientForm(request.POST)
        cl = Person()
        if (form.is_valid()):
            cl= Person.update_client(cl, request, pk, data)
        return redirect('admin_client', pk)


class Delete_user(DeleteView):
    model = Person
    context_object_name = 'client'

    def post(self, request, pk):
        is_delete = Person.delete_user(pk)
        user = Person.objects.get(id=pk)
        if (is_delete):
            if (user.Position==2):
                return redirect('admin_clients')
            elif (user.Position==1):
                return redirect('admin_clients')
            else:
                return redirect('admin_admins')
        return pk


class Show_client_orders(DetailView):
    model = Person
    template_name = 'user_and_company/admin_client_orders.html'
    context_object_name = 'client'


class Show_admins_list(ListView):
    model = Person
    template_name = 'user_and_company/admin_users.html'
    context_object_name = 'adminget'
    queryset = Person.objects.filter(DateDel = None, Position =0)


class Show_admin(DetailView):
    model = Person
    template_name = 'user_and_company/admin_info_user.html'
    context_object_name = 'admin'

class Add_admin(CreateView):
    form_class = AdminForm
    template_name = 'user_and_company/admin_add_user.html'

    def post(self, request):
        form = AdminForm(request.POST)
        if (form.is_valid()):
            cl = Person()
            cl= Person.add_admin(cl, request)
        return redirect('admin_admins')


class Update_admin(UpdateView):
    model = Person
    form_class = AdminForm
    template_name = 'user_and_company/admin_update_user.html'
    context_object_name = 'admin'

    def post(self, request, pk):
        form = AdminForm(request.POST)
        cl = Person()
        if (form.is_valid()):
            cl= Person.update_admin(cl, request, pk)
        return redirect('admin_admin', pk)


class Show_companies_list(ListView):
    model = Company
    template_name = 'user_and_company/admin_companies.html'
    context_object_name = 'companyget'
    queryset = Company.objects.filter(DateDel = None)


class Show_company(DetailView):
    model = Company
    template_name = 'user_and_company/admin_info_company.html'
    context_object_name = 'company'


class Add_company(CreateView):
    form_class = CompanyForm
    template_name = 'user_and_company/admin_add_company.html'

    def post(self, request):
        form = CompanyForm(request.POST)
        if (form.is_valid()):
            cl = Company()
            cl= Company.add_company(cl, request)
        return redirect('admin_companies')


class Update_company(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'user_and_company/admin_update_company.html'
    context_object_name = 'company'

    def post(self, request, pk):
        form = CompanyForm(request.POST)
        cl = Person()
        if (form.is_valid()):
            cl= Company.update_company(cl, request, pk)
        return redirect('admin_company', pk)


class Delete_company(DeleteView):
    model = Company
    context_object_name = 'company'

    def post(self, request, pk):
        is_delete = Company.delete_company(pk)
        if (is_delete):
            return redirect('admin_companies')
        return pk


class Show_company_cars(DetailView):
    model = Company
    template_name = 'user_and_company/admin_company_cars.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        ctx = super(Show_company_cars, self).get_context_data(**kwargs)

        company = Company.objects.get(id = self.kwargs['pk'])
        carget = Car.objects.filter(CompanyID_id = company.id, DateDel = None)
        js = {}
        for x in carget:
            js[x.id] = json.loads(x.Photos)

        paginator = Paginator(carget, 10)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev = '?page={}'.format(page.previous_page_number())
        else:
            prev = ''
        if page.has_next():
            next = '?page={}'.format(page.next_page_number())
        else:
            next = ''
        ctx = {
            'company' : company,
            'js' : js,
            'carget' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }
        return ctx


class Show_company_orders(DetailView):
    model = Company
    template_name = 'user_and_company/admin_company_orders.html'
    context_object_name = 'company'

    def get_context_data(self, **kwargs):
        ctx = super(Show_company_orders, self).get_context_data(**kwargs)

        company = Company.objects.get(id = self.kwargs['pk'])

        dict = company.car_set.filter(DateDel = None)
        orderget = []
        for c in dict:
            orderget.extend(list(c.car.all()))
        paginator = Paginator(orderget, 10)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev = '?page={}'.format(page.previous_page_number())
        else:
            prev = ''
        if page.has_next():
            next = '?page={}'.format(page.next_page_number())
        else:
            next = ''
        ctx = {
            'company' : company,
            'orderget' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next
        }
        return ctx


class Show_employees_list(DetailView):
    model = Company
    template_name = 'user_and_company/admin_employees.html'
    context_object_name = 'company'


class Add_employee(CreateView):
    form_class = AdminForm
    template_name = 'user_and_company/admin_add_employee.html'
    context_object_name = 'w'

    def get_context_data(self, **kwargs):
        c=Company.objects.get(pk=self.kwargs['pk'])
        ctx = super(Add_employee, self).get_context_data(**kwargs)
        ctx['company'] = c
        return ctx

    def post(self, request, pk):
        form = AdminForm(request.POST)

        if (form.is_valid()):
            cl = Person()
            cl= Person.add_employee(cl, request, pk)
        return redirect('admin_employees', pk)


class Show_employee(DetailView):
    model = Person
    template_name = 'user_and_company/admin_info_employee.html'
    context_object_name = 'employee'
    pk_url_kwarg = 'employee_id'


class Update_employee(UpdateView):
    model = Person
    form_class =AdminForm
    template_name = 'user_and_company/admin_update_employee.html'
    context_object_name = 'employee'
    pk_url_kwarg = 'employee_id'

    def post(self, request, pk, employee_id):
        form = AdminForm(request.POST)
        cl = Person()
        if (form.is_valid()):
            cl= Person.update_admin(cl, request, employee_id)
        return redirect('admin_employee', pk, employee_id)


class Delete_employee(DeleteView):
    model = Person
    context_object_name = 'employee'

    def post(self, request, pk, employee_id):
        is_delete = Person.delete_user(employee_id)
        if (is_delete):
            return redirect('admin_employees', pk)
        return pk
