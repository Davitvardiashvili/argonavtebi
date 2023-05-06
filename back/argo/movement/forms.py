from django.forms import ModelForm
from .models import HomePage, ServicesPage, Gallery, AboutPage, ContactPage


class HomeForm(ModelForm):
    class Meta:
        model = HomePage
        fields = ['side_picture', 'title', 'text1', 'text2', 'text3']
        labels = {'side_picture': 'Image', 'title': 'title', 'text1': 'text1', 'text2': 'text2', 'text3': 'text3'}


class ServicesForm(ModelForm):
    class Meta:
        model = ServicesPage
        fields = ['title', 'text']
        labels = {'title': 'title', 'text': 'text'}


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['images']
        labels = {'images': 'Image'}


class AboutForm(ModelForm):
    class Meta:
        model = AboutPage
        fields = ['title', 'text']
        labels = {'title': 'title', 'text': 'text'}


class ContactForm(ModelForm):
    class Meta:
        model = ContactPage
        fields = ['title', 'address', 'mobile_number', 'email']
        labels = {'title': 'title', 'address': 'address', 'mobile_number': 'mobile_number', 'email': 'email'}
