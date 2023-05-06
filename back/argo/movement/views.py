from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import HomePage, ServicesPage, Gallery, AboutPage, ContactPage
from .forms import HomeForm, ServicesForm, GalleryForm, AboutForm, ContactForm
from django.template import loader
from django.http import HttpResponseRedirect
from django.http import HttpResponse


@login_required(login_url='login')
def home(request, id=1):
    if id:
        obj = HomePage.objects.get(id=id)
    else:
        obj = HomePage()

    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeForm(instance=obj)

    context = {
        'form': form, 'obj': obj
    }
    return render(request, 'movement/home.html', context)


@login_required(login_url='login')
def services(request):
    form = ServicesForm()
    servic = ServicesPage.objects.all()
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    context = {
        'form': form, 'servic': servic
    }
    return render(request, 'movement/services.html', context)


@login_required(login_url='login')
def update_services(request, id):
    servic = ServicesPage.objects.get(id=id)
    form = ServicesForm(instance=servic)
    template = loader.get_template('movement/update-service.html')
    if request.method == 'POST':
        form = ServicesForm(request.POST, instance=servic)
        if form.is_valid():
            form.save()
            return redirect('services')
    context = {
        'form': form, 'servic': servic
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def delete_services(request, id):
    servic = ServicesPage.objects.get(id=id)
    if request.method == "POST":
        servic.delete()
        return redirect('services')
    return render(request, 'movement/delete.html', {'obj': servic})



@login_required(login_url='login')
def gallery(request):
    form = GalleryForm()
    context = {
        'form': form
    }
    return render(request, 'movement/gallery.html', context)


@login_required(login_url='login')
def about(request):
    form = AboutForm()
    context = {
        'form': form
    }
    return render(request, 'movement/about.html', context)


@login_required(login_url='login')
def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'movement/contact.html', context)
