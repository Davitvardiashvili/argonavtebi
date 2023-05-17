from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default="user.png")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class HomePage(models.Model):
    side_picture = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    text1 = models.TextField(max_length=1000, blank=True, null=True)
    text2 = models.TextField(max_length=1000, blank=True, null=True)
    text3 = models.TextField(max_length=1000, blank=True, null=True)


class ServicesPage(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.title} \n {self.text}'


class Gallery(models.Model):
    images = models.ImageField(upload_to='images',default="user.png")


class AboutPage(models.Model):
    text = models.TextField(max_length=1000, blank=True, null=True)


class ContactPage(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)


class SideImages(models.Model):
    images = models.ImageField(upload_to='images',default="user.png")