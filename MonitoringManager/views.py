from django.shortcuts import render, redirect
from .models import Websites
from .forms import WebsitePostForm
from django.contrib import messages


# Create your views here.

def home_view(request):
    return render(request,
                  'about.html'
                  )


def websites_list(request):
    Sites = Websites.objects.all()

    return render(request,
                  'websitesList.html',
                  {'Sites': Sites}
                  )


def add_website(request):
    if request.method == 'POST':
        form = WebsitePostForm(request.POST)
        if form.is_valid():
            if Websites.objects.filter(urlAddress=form.cleaned_data['urlAddress'],
                                       intervals=form.cleaned_data['intervals']):
                messages.warning(request, 'Już dodano stronę z takim interwałem')
            else:
                form.save()
                messages.info(request, 'Pomyślnie dodano domenę.')
                return redirect('/websites')
    else:
        form = WebsitePostForm()
    return render(request,
                  'addWebsite.html',
                  {'form': form})


def check_website(request, number):
    return render(request,
                  'checkWebsite.html',
                  {'number': number}
                  )


def edit_website(request, number):
    return render(request,
                  'editWebsite.html',
                  {'number': number}
                  )


def not_working_websites(request):
    render(request,
           'notWorkingWebsites.html'
           )
