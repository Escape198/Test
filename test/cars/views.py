from typing import Counter
import json

from cars.forms import CarForm
from user_and_company.models import Company
from .models import Car
from .models import Category

from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.core.paginator import Paginator


class Show_catalog_list(ListView):
    model = Category
    template_name = 'cars/catalog.html'
    context_object_name = 'catalogget'


class Show_car_list(DetailView):
    model = Category
    template_name = 'cars/carlist.html'
    context_object_name = 'cat'

    def get_context_data(self, **kwargs):
        ctx = super(Show_car_list, self).get_context_data(**kwargs)
        sort = self.request.GET.get('sort', 'Brand_and_name')
        cat = Category.objects.get(id =self.kwargs['pk'])
        carget = Car.objects.filter(CategoryID_id = cat.id, Status = 0)
        if sort != '':
            carget = carget.order_by(sort)
        js = {}
        for x in carget:
            js[x.id] = json.loads(x.Photos)
        count = self.request.GET.get('count', 5)
        paginator = Paginator(carget, count)
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
            'cat' : cat,
            'js' : js,
            'carget' : page,
            'is_paginated' : is_paginated,
            'prev' : prev,
            'next' : next,
            'count' : int(count),
            'sort' : sort
        }
        return ctx


class Cars_datail_view(DetailView):
    model = Car
    template_name = 'cars/carcard.html'
    context_object_name = 'car_item'

    def get_context_data(self, **kwargs):
        ctx = super(Cars_datail_view, self).get_context_data(**kwargs)
        car = Car.objects.get(id = self.kwargs['pk'])

        m = json.loads(car.Photos)
        ctx['m'] = m
        ctx['f'] = list(m)
        return ctx


class Show_cars_list(ListView):
    model = Car
    template_name = 'cars/admin_catalog.html'
    context_object_name = 'carget'

    def get_context_data(self, **kwargs):
        ctx = super(Show_cars_list, self).get_context_data(**kwargs)
        carget = Car.objects.filter(DateDel = None)
        categories = Category.objects.all()
        companies = Company.objects.filter(DateDel = None)

        js = {}
        for x in carget:
            js[x.id] = json.loads(x.Photos)

#filters
        company = self.request.GET.get('company', '')
        if company != '' and company is not None :
            carget = carget.filter(CompanyID_id = company)
            ctx['company'] = int(company)
        else:
            ctx['company'] = company

        category = self.request.GET.get('category', '')
        if category != '' and category is not None :
            carget = carget.filter(CategoryID_id = category)
            ctx['category'] = int(category)
        else:
            ctx['category'] = category

        price_from = self.request.GET.get('price_from', '')
        if price_from != '' and price_from is not None :
            carget = carget.filter(Price__gte = price_from)
            ctx['price_from'] = int(price_from)

        price_to = self.request.GET.get('price_to', '')
        if price_to != '' and price_to is not None :
            carget = carget.filter(Price__lte = price_to)
            ctx['price_to'] = int(price_to)
#search
        search_type = 'car_name'
        search = self.request.GET.get('search', '')
        if search != '' and search is not None:
            if self.request.GET.get('car_search') == 'car_name' :
                carget = carget.filter(Brand_and_name__icontains = search)
                ctx['search_type'] = search_type

            if self.request.GET.get('car_search') == 'id' :
                carget = carget.filter(id = search)
                search_type = 'id'
                ctx['search_type'] = search_type


        count = self.request.GET.get('count', 5)
        paginator = Paginator(carget, count)
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

        ctx['js'] = js
        ctx['carget'] = page
        ctx['is_paginated'] = is_paginated
        ctx['prev' ]= prev
        ctx['next'] = next
        ctx['count'] = int(count)
        ctx['companies'] = companies
        ctx['categories'] = categories
        ctx['query'] = '&search=' + search + '&car_search=' + search_type +'&company=' + company + '&category=' + category + '&price_from=' + price_from + '&price_to=' + price_to

        print(ctx)
        return ctx


class Add_car(CreateView):
    form_class = CarForm
    template_name = 'cars/admin_add_car.html'
    category = Category.objects.all()
    company = Company.objects.all()
    cl = Car()

    def post(self, request):
        print(request.FILES.getlist('photo'))
        x = FileSystemStorage(location='media/car_photo')
        di = {}
        for f in request.FILES.getlist('photo'):
            p = f.read()
            x.save(f.name, f)
            di['/media/car_photo/' + f.name] = f.name
            print(di)

        form = CarForm(request.POST)
        if (form.is_valid):
            cl = Car()
            cl= Car.add_car(cl, request, json.dumps(di))
        return redirect('admin_cars')

    def get_context_data(self, **kwargs):
        ctx = super(Add_car, self).get_context_data(**kwargs)
        ctx['car'] = self.cl
        ctx['category'] = self.category
        ctx['company'] = self.company
        return ctx


class Update_car(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/admin_update_car.html'
    context_object_name = 'car'
    category = Category.objects.all()
    company = Company.objects.all()

    def post(self, request, pk):
        form = CarForm(request.POST)
        if (form.is_valid()):
            cl = Car()
            cl= Car.update_car(cl, request, pk)

        if (request.POST.get('Hidden') != None):
            car = Car()
            car = Car.hidden_car(pk)

        if (request.POST.get('Visible') != None):
            car = Car()
            car = Car.visible_car(pk)

        return redirect('admin_cars')

    def get_context_data(self, **kwargs):
        ctx = super(Update_car, self).get_context_data(**kwargs)
        ctx['category'] = self.category
        ctx['company'] = self.company
        return ctx


class Delete_car(DeleteView):
    model = Car
    context_object_name = 'car'

    def post(self, request, pk):
        is_delete = Car.delete_car(pk)
        if (is_delete):
            return redirect('admin_cars')
        return pk
