from django.db.models import fields
from .models import Company, Person
from django import forms


class ClientForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('Name', 'Fname', 'Phone', 'Passport', 'NumVU')


class AdminForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('Name', 'Fname', 'Email', 'Phone', 'Comment')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('Name', 'Email', 'Phone', 'Note', 'ContactFIO', 'ContactEmail', 'ContactPhone')
