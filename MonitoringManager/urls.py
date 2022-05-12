from django.contrib import admin
from django.urls import path, include
from .views import home_view, websites_list, add_website, check_website, edit_website

app_name = 'MonitoringManager'
urlpatterns = [
    path('', home_view, name='home-view'),
    path('websites', websites_list, name='websites-list'),
    path('websites/<int:number>/', check_website, name='websites-check'),
    path('websites/<int:number>/edit/', websites_list, name='websites-edit'),
    path('add', add_website, name='websites-add'),
]
