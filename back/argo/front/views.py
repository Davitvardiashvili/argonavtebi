from django.shortcuts import render
from movement.models import HomePage,ServicesPage,Gallery,AboutPage,ContactPage,SideImages
from .forms import ContactForm
from django.core.mail import send_mail



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

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            mail_subject = f'Contact Form Submission - {subject}'
            mail_body = f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'
            send_mail(mail_subject, mail_body, email, ['davit.vardiashviliwork@gmail.com'])
            return render(request, 'front/index.html')
    else:
        form = ContactForm()





    context = {
        'home': home,
        'services':services,
        'gallery':gallery,
        'abouts':abouts,
        # 'form':form,
        'contact':contact,
        'side_image_1':side_image_1,
        'side_image_2':side_image_2,
        'side_image_3':side_image_3,
        'side_image_4':side_image_4
    }
    return render(request, 'front/index.html', context)
