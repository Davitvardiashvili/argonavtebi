from django.urls import path, include
from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('panel/', views.home, name='home'),
    path('panel/services/', views.services, name='services'),
    path('panel/edit_services/<id>', views.update_services, name='update-services'),
    path('panel/delete_services/<id>', views.delete_services, name='delete-services'),
    path('panel/gallery/', views.gallery, name='gallery'),
    path('panel/about/', views.about, name='about'),
    path('panel/contact/', views.contact, name='contact'),
]
