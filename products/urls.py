from django.conf.urls import url
from . import views

#subURLS ex. productos/1
urlpatterns = [
    url(r'^$',views.home, name='home'),#productos/
    url(r'^(?P<familia_id>[0-9]+)$', views.familyDetails, name='familyDetails')
]