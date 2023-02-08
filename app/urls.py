from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('user', views.account_details, name='User'),
    path('transfer', views.transfer, name='Transfer')
]