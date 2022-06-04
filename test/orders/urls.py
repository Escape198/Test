from django.urls import path
from django.urls.conf import include

from . import views


urlpatterns=[
    path('', views.Show_orders_list.as_view(), name='admin_orders'),
    path('order_<int:pk>', views.Show_order.as_view(), name='admin_order'),
    path('add_order', views.Add_order.as_view(), name='admin_add_order'),
    path('order_<int:pk>/update', views.Update_order.as_view(), name='admin_update_order'),
    path('add_order_client_<int:pk>', views.Add_order_client.as_view(), name='admin_add_order_client'),

    path('messages', views.Show_messages_list.as_view(), name='admin_messages'),

    path('order_<int:order_id>/comment_<int:pk>_delete', views.Delete_comment.as_view(), name='admin_delete_comment')
    ]
