from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('home/<int:w_id>/', views.delete, name='delete'),
]

