from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainpage, name='main'),
    # path('contact/', views.contact, name='contact'),
]