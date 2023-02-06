from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'Index'),
    path('user/<int:id>', views.user_by_id, name='user_by_id')
]