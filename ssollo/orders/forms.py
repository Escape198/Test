from django.db.models import fields
from django import forms

from .models import Contract


class OrderForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('Client', 'Car', 'DateStartContract', 'DateEndContract', 'Driver',  'Cost', 'Note' )


class Order_update_Form(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('Car', 'DateStartContract', 'DateEndContract', 'Driver',  'Cost', 'Note' )
