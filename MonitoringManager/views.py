from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Websites
from .forms import WebsitePostForm
from django.contrib import messages
from urllib.parse import urlparse


# Create your views here.

def home_view(request):
    return render(request,
                  'about.html'
                  )


def websites_list(request):
    sites = get_list_or_404(Websites)
    return render(request,
                  'websitesList.html',
                  {'Sites': sites}
                  )


def add_website(request):
    if request.method == 'POST':
        form = WebsitePostForm(request.POST)
        if form.is_valid():

            if Websites.objects.filter(urlAddress=form.cleaned_data['urlAddress'],
                                       intervals=form.cleaned_data['intervals']):
                messages.error(request, 'Już dodano stronę z takim interwałem')
            else:
                form.save()
                messages.success(request, 'Pomyślnie dodano domenę.')
                return redirect('/websites')
    else:
        form = WebsitePostForm()
    return render(request,
                  'addWebsite.html',
                  {'form': form})


def check_website(request, id=None):
    return render(request,
                  'checkWebsite.html',
                  {'id': id}
                  )


def edit_website(request, id=None):
    site = get_object_or_404(Websites, id=id)
    if request.method == 'POST':
        form = WebsitePostForm(request.POST)
        if form.is_valid():
            old_site = get_object_or_404(Websites, id=id)
            old_site.name = form.cleaned_data['name']
            old_site.intervals = form.cleaned_data['intervals']
            old_site.urlAddress = form.cleaned_data['urlAddress']
            old_site.isWorking = form.cleaned_data['isWorking']
            old_site.save()
            return redirect('MonitoringManager:websites-list')
    else:
        form = WebsitePostForm(initial={'name': site.name,
                                    'urlAddress': site.urlAddress,
                                    'intervals': site.intervals})
    return render(request,
                  'editWebsite.html',
                  {'site': site.name,
                   'form': form}
                  )


def delete_website(request, id=None):
    object = get_object_or_404(Websites, id=id)
    object.delete()
    return redirect('MonitoringManager:websites-list')


def not_working_websites(request):
    sites = Websites.objects.filter(isWorking=False)
    render(request,
           'notWorkingWebsites.html',
           {'Sites': sites}
           )
