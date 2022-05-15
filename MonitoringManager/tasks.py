from __future__ import absolute_import, unicode_literals
from .models import Websites, Events
from celery import shared_task
import requests, hashlib


@shared_task
def checkWebsites(*args, **kwargs):
    concatenate = "".join(args)
    websites = Websites.objects.get_queryset().filter(intervals=concatenate)
    for site in websites:
        try:
            response = requests.get(site.urlAddress)
            if response.status_code in range(199, 299, 1):
                site.isWorking = True
            else:
                site.isWorking = False
            md5 = hashlib.md5(response.text.encode()).hexdigest()
            Events.objects.create(websiteId=site, returnCode=response.status_code, md5=md5)
        except requests.exceptions.ConnectionError:
            site.isWorking = False
            md5 = "Connection Error"
            Events.objects.create(websiteId=site, returnCode='503', md5=md5)
        site.save()
