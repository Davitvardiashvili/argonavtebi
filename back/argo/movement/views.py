from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import HomePage, ServicesPage, Gallery, AboutPage, ContactPage,SideImages
from .forms import HomeForm, ServicesForm, GalleryForm, AboutForm, ContactForm,SideImagesForm
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
    images = Gallery.objects.all()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    context = {
        'form': form,
        'images': images,
    }
    return render(request, 'movement/gallery.html', context)

@login_required(login_url='login')
def edit_gallery(request,id):
    gallery = Gallery.objects.get(id=id)
    form = GalleryForm(instance=gallery)
    template = loader.get_template('movement/update-'
                                   'gallery.html')
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    context = {'gallery':gallery,'form':form}
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def delete_gallery(request,id):
    gallery = Gallery.objects.get(id=id)
    if request.method == "POST":
        gallery.delete()
        return redirect('gallery')
    return render(request, 'movement/delete.html', {'obj': gallery})


@login_required(login_url='login')
def about(request):
    form = AboutForm()
    abouts = AboutPage.objects.all()
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
    context = {
        'form': form,
        'abouts':abouts
    }
    return render(request, 'movement/about.html', context)


@login_required(login_url='login')
def update_about(request,id):
    about = AboutPage.objects.get(id=id)
    form = AboutForm(instance=about)
    template = loader.get_template('movement/update-about.html')
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about')
    context = {
        'form': form, 'about': about
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def delete_about(request,id):
    abouts = AboutPage.objects.get(id=id)
    if request.method == "POST":
        abouts.delete()
        return redirect('about')
    return render(request, 'movement/delete.html', {'obj': abouts})


@login_required(login_url='login')
def contact(request, id=1):
    if id:
        obj = ContactPage.objects.get(id=id)
    else:
        obj = ContactPage()

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm(instance=obj)
    context = {
        'form': form
    }
    return render(request, 'movement/contact.html', context)

@login_required(login_url='login')
def side_images(request):
    form = SideImagesForm()
    images = SideImages.objects.all()
    # if request.method == 'POST':
    #     form = SideImagesForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('side-images')
    context = {
        'form': form,
        'images': images,
    }
    return render(request, 'movement/side_images.html', context)


@login_required(login_url='login')
def edit_side_images(request,id):
    side_image = SideImages.objects.get(id=id)
    form = SideImagesForm(instance=side_image)
    template = loader.get_template('movement/update-'
                                   'side_images.html')
    if request.method == "POST":
        form = SideImagesForm(request.POST, request.FILES, instance=side_image)
        if form.is_valid():
            form.save()
            return redirect('side-images')
    context = {'side_image':side_image,'form':form}
    return HttpResponse(template.render(context, request))