from django.contrib import admin

from .models import Person
from .models import Company


admin.site.register(Person)
admin.site.register(Company)
