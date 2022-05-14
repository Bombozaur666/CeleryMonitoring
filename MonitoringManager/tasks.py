from __future__ import absolute_import, unicode_literals
from .models import Websites, Events
from celery import shared_task
import requests


@shared_task
def checkWebsites(*args, **kwargs):
    concatenate = "".join(args)
    websites = Websites.objects.get_queryset().filter(intervals=concatenate)
    for site in websites:
        response = requests.head(site.urlAddress)
        print(response)
        if response.status_code in range(199, 299, 1):
            site.isWorking = True
            site.save()
        else:
            site.isWorking = False
            site.save()
            Events.objects.create(websiteId=site, returnCode=response.status_code)
