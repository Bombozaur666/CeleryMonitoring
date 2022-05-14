from django.core.validators import URLValidator
from django.db import models


# Create your models here.
# My own model Manager for easier filtering


class Websites(models.Model):
    name = models.CharField("Nazwa domeny",
                            max_length=200)
    urlAddress = models.URLField("Adres URL",
                                  max_length=1000
                                 )
    TIME_INTERVALS = [
        ('01', '1 minute'),
        ('05', '5 minutes'),
        ('15', '15 minutes'),
        ('30', '30 minutes'),
        ('60', '60 minutes'),
    ]
    intervals = models.CharField("Interwały czasowe",
                                 choices=TIME_INTERVALS,
                                 max_length=5,
                                 default='01', )
    isWorking = models.BooleanField("Czy działa",
                                    default=True,
                                    blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('intervals', 'name')


class Events(models.Model):
    websiteId = models.ForeignKey(Websites,
                                  on_delete=models.CASCADE,
                                  related_name='events')
    returnCode = models.CharField("Kod błędu", max_length=3)
    time = models.DateTimeField("Data zdażenia", auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('websiteId', 'time')



