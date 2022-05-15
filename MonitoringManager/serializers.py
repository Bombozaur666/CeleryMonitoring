from rest_framework import serializers
from .models import Websites, Events


class WebsitesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Websites
        fields = ['id', 'name', 'urlAddress', 'intervals', 'isWorking']


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    websiteId = WebsitesSerializer()

    class Meta:
        model = Events
        fields = ['id', 'websiteId', 'returnCode', 'md5']
