from django.urls import path
from . import views


urlpatterns=[
    path('', views.Show_catalog_list.as_view(), name='catalog'),
    path('category_<int:pk>/', views.Show_car_list.as_view(), name='carlist'),
    path('category_<int:category_id>/<int:pk>', views.Cars_datail_view.as_view(), name='cars_detail'),
    ]
