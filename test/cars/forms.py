from django import forms
from django.db.models import fields

from .models import Car, Category


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('Header', 'CategoryID', 'CompanyID', 'Brand_and_name', 'Car_type', 'Engine', 'Transmission', 'Drive', 'Wheel_drive', 'Year', 'Driver', 'Power', 'Price', 'FixedRate', 'Percent','Location', 'RentCondition')
