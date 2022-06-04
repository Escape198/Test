from django.urls import path
from . import views


urlpatterns=[
    path('cars/', views.Show_cars_list.as_view(), name='admin_cars'),
    path('cars/add_car', views.Add_car.as_view(), name='admin_add_car'),
    path('cars/<int:pk>', views.Cars_datail_view.as_view(), name='admin_info_car'),
    path('cars/<int:pk>/update', views.Update_car.as_view(), name='admin_update_car'),
    path('cars/<int:pk>/delete', views.Delete_car.as_view(), name='admin_delete_car')
    ]
