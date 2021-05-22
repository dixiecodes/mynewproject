from django.urls import path 

from . import views

urlpatterns = [
    path('', views.infopage_index, name= 'infopage_index'),
]