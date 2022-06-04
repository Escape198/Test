from django.urls import path
from django.urls.conf import include

from . import views


urlpatterns=[
    path('', views.admin_start, name='start_admin'),
    path('users/', include('user_and_company.urls')),
    path('catalog/', include('cars.urls_ad')),
    path('orders/', include('orders.urls')),
    path('feedback/', include('feedback_and_comments.urls'))
    ]
