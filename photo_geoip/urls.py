from django.conf.urls import patterns, include, url
from photo_geoip.views import Webhook, YourTours

urlpatterns = patterns('',
    url(r'^webhook/$', Webhook.as_view(), name='webhook'),
    url(r'^your-tours/$', YourTours.as_view(), name='your_tours'),
)