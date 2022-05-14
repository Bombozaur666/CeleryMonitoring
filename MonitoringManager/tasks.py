from __future__ import absolute_import, unicode_literals
from .models import Websites, Events
from celery import shared_task
import requests, hashlib


@shared_task
def checkWebsites(*args, **kwargs):
    concatenate = "".join(args)
    websites = Websites.objects.get_queryset().filter(intervals=concatenate)
    for site in websites:
        response = requests.get(site.urlAddress)
        md5 = hashlib.md5(response.text.encode()).hexdigest()
        if response.status_code in range(199, 299, 1):
            site.isWorking = True
        else:
            site.isWorking = False
        Events.objects.create(websiteId=site, returnCode=response.status_code, md5=md5)
        site.save()
