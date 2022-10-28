from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasklist', views.tasklist, name='tasklist'),
    path('app_download', views.app_download, name='app_download'),

]
