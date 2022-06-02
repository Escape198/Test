from django.urls import path
from django.urls.conf import include

from . import views


urlpatterns=[
    path('', views.Show_feedback_list.as_view(), name='admin_feedback'),
    path('feedback/<int:pk>/delete', views.Delete_feedback.as_view(), name='admin_delete_feedback'),
    path('feedback/<int:pk>/update', views.Update_feedback.as_view(), name='admin_update_feedback')
    ]
