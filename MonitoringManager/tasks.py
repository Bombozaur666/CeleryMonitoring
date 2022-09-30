from __future__ import absolute_import, unicode_literals

import hashlib
import requests
from celery import shared_task
from django.core.mail import send_mail

from .models import Websites, Events

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

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
            parsed_html = BeautifulSoup(response.text.encode())
            registered = parsed_html.body.find('span', attrs={'class': 'registered'}).text
            if int(registered) != 14:
                subject = f'SPRAWDZ REJESTRACJE - JEST {registered} ZAREJESTROWANYCH'
                message = f'ZAPIERDALASZ W PODSKOKACH'
                send_mail(subject, message, 'django.celery@outlook.com', ['bibprz@st.amu.edu.pl'])
            Events.objects.create(websiteId=site, returnCode=response.status_code, md5=registered)
        except requests.exceptions.ConnectionError:
            site.isWorking = False
            md5 = "Connection Error"
            Events.objects.create(websiteId=site, returnCode='503', md5=md5)
        site.save()
