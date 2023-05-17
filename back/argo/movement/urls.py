from django.urls import path, include
from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('panel/', views.home, name='home'),
    path('panel/services/', views.services, name='services'),
    path('panel/edit_services/<id>', views.update_services, name='update-services'),
    path('panel/delete_services/<id>', views.delete_services, name='delete-services'),
    path('panel/gallery/', views.gallery, name='gallery'),
    path('panel/edit_gallery/<id>', views.edit_gallery, name='update-gallery'),
    path('panel/delete_gallery/<id>', views.delete_gallery, name='delete-gallery'),
    path('panel/about/', views.about, name='about'),
    path('panel/edit_about/<id>', views.update_about, name='update-about'),
    path('panel/delete_about/<id>', views.delete_about, name='delete-about'),
    path('panel/contact/', views.contact, name='contact'),
    path('panel/side_images/', views.side_images, name='side-images'),
    path('panel/edit_side_images/<id>', views.edit_side_images, name='update-side-images'),
]
