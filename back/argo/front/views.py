from django.shortcuts import render
from movement.models import HomePage,ServicesPage


def mainpage(request):
    home = HomePage.objects.get(pk=1)
    services = ServicesPage.objects.all()
    context = {
        'home': home,
        'services':services,

    }
    return render(request, 'front/index.html', context)
