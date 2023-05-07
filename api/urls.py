from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('data/', views.getData, name='data-it'),
    path('data/<str:pk>/', views.getAccount, name='acc')
]