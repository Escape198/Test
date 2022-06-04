from django.conf.urls import include
from django.urls import path

from . import views


urlpatterns=[
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('rentcondition/', views.Rentcondition, name='Rentcondition'),

    path('contact/add_feedback', views.Add_feedback.as_view(), name='contact_add_feedback')
    ]
