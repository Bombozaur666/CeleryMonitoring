from rest_framework import serializers
from .models import Websites, Events


class WebsitesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Websites
        fields = ['name', 'UrlAddress', 'intervals', 'isWorking']


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ['websiteId', 'returnCode']
