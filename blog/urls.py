from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.post_list, name = 'post_list'),
    path(r'^post/(?P<pk>\d+)/$', views.post_detail,name = 'post_detail')
    ]