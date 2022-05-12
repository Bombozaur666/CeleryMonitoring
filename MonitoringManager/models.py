from django.db import models


# Create your models here.
class Websites(models.Model):
    name = models.CharField(max_length=200)
    urlAddress = models.CharField(max_length=1000)
    TIME_INTERVALS = [
        ('1MIN', '1 minute'),
        ('5MIN', '5 minutes'),
        ('15MIN', '15 minutes'),
        ('30MIN', '30 minutes'),
        ('60MIN', '60 minutes'),
    ]
    intervals = models.CharField(choices=TIME_INTERVALS,
                                 max_length=5,
                                 default='1MIN', )
    isWorking = models.BooleanField(default=True,
                                    blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('urlAddress',)


class Events(models.Model):
    websiteId = models.ForeignKey(Websites,
                                  on_delete=models.CASCADE,
                                  related_name='events')
    returnCode = models.CharField(max_length=3)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('websiteId',)

