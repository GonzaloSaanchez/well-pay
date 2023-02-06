from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Index'),
    path('user', views.user_details, name='User')
]