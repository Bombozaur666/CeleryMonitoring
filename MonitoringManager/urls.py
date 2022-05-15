from django.urls import path, include
from .views import home_view, websites_list, add_website, check_website, edit_website, not_working_websites, delete_website, WebsiteViewSet, EventViewSet, NotWorkingWebsiteViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('websitesApi', WebsiteViewSet)
router.register('notworkingApi', NotWorkingWebsiteViewSet)
router.register('eventsApi', EventViewSet)

app_name = 'MonitoringManager'

urlpatterns = [
    path('', include(router.urls)),
    path('', home_view, name='home-view'),
    path('websites', websites_list, name='list-of-sites'),
    path('websites/<int:id>/', check_website, name='websites-check'),
    path('websites/<int:id>/edit/', edit_website, name='websites-edit'),
    path('websites/notworking/', not_working_websites, name='websites-not-working'),
    path('websites/<int:id>/delete/', delete_website, name='websites-delete'),
    path('websites/add', add_website, name='websites-add'),

]
