from django.contrib import admin

from .models import Car
from .models import Category


admin.site.register(Car)
admin.site.register(Category)
