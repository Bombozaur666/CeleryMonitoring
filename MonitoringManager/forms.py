from django import forms
from .models import Websites


class WebsitePostForm(forms.ModelForm):
    class Meta:
        model = Websites
        fields = ('name', 'urlAddress', 'intervals', 'isWorking')

