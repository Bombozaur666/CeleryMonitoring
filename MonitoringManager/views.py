from django.shortcuts import render, redirect, get_object_or_404
from .models import Websites, Events
from .forms import WebsitePostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from .serializers import WebsitesSerializer, EventsSerializer


# Create your views here.

def home_view(request):
    return render(request,
                  'about.html'
                  )


def websites_list(request):
    all_sites = Websites.objects.all()
    paginator = Paginator(all_sites, 20)
    page = request.GET.get('page')
    try:
        sites = paginator.page(page)
    except PageNotAnInteger:
        sites = paginator.page(1)
    except EmptyPage:
        sites = paginator.page(paginator.num_pages)
    return render(request,
                  'websitesList.html',
                  {'sites': sites,
                   'page': page}
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
    name = get_object_or_404(Websites, id=id).name
    all_events = Events.objects.filter(websiteId=id)
    paginator = Paginator(all_events, 20)
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(request,
                  'checkWebsite.html',
                  {'events': events,
                   'name': name}
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
            return redirect('MonitoringManager:list-of-sites')
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
    get_object_or_404(Websites, id=id).delete()
    return redirect('MonitoringManager:list-of-sites')


def not_working_websites(request):
    all_sites = Events.objects.filter(websiteId__isWorking__exact=False).order_by('websiteId_id').distinct('websiteId_id')
    paginator = Paginator(all_sites, 20)
    page = request.GET.get('page')
    try:
        sites = paginator.page(page)
    except PageNotAnInteger:
        sites = paginator.page(1)
    except EmptyPage:
        sites = paginator.page(paginator.num_pages)
    return render(request,
                  'notWorkingWebsites.html',
                  {'sites': sites}
                  )


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Websites.objects.all()
    serializer_class = WebsitesSerializer


class NotWorkingWebsiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Websites.objects.filter(isWorking=False)
    serializer_class = WebsitesSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


