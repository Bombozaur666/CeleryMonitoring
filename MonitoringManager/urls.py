from django.contrib import admin
from django.urls import path, include
from .views import home_view, websites_list, add_website, check_website, edit_website, not_working_websites, delete_website

app_name = 'MonitoringManager'
urlpatterns = [
    path('', home_view, name='home-view'),
    path('websites', websites_list, name='websites-list'),
    path('websites/<int:id>/', check_website, name='websites-check'),
    path('websites/<int:id>/edit/', edit_website, name='websites-edit'),
    path('websites/notworking/', not_working_websites, name='websites-not-working'),
    path('websites/<int:id>/delete/', delete_website, name='websites-delete'),
    path('add', add_website, name='websites-add'),
]
