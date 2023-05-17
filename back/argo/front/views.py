from django.shortcuts import render
from movement.models import HomePage,ServicesPage,Gallery,AboutPage,ContactPage,SideImages
import requests
from .forms import ContactForm
from django.core.mail import send_mail


def send_to_telegram(message):

    apiToken = '6291820566:AAEph2zox4gBu3l6kwYLt8KTdmyPZLvwlj4'
    chatID = '-932176749'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)




def mainpage(request):
    home = HomePage.objects.get(pk=1)
    services = ServicesPage.objects.all()
    gallery = Gallery.objects.all()
    abouts = AboutPage.objects.all()
    contact = ContactPage.objects.get(pk=1)
    side_image_1 = SideImages.objects.get(pk=1)
    side_image_2 = SideImages.objects.get(pk=2)
    side_image_3 = SideImages.objects.get(pk=3)
    side_image_4 = SideImages.objects.get(pk=4)







    context = {
        'home': home,
        'services':services,
        'gallery':gallery,
        'abouts':abouts,
        'contact':contact,
        'side_image_1':side_image_1,
        'side_image_2':side_image_2,
        'side_image_3':side_image_3,
        'side_image_4':side_image_4
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            entire = f'Subject: {subject}\n' \
                     f'Email address: {email}\n' \
                     f'Name: {name}\n' \
                     f'Message: {message}'
            send_to_telegram(entire)

            return render(request, 'front/index.html', context)
    else:
        form = ContactForm()

    return render(request, 'front/index.html', context)
