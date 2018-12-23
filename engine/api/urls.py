from django.conf import settings
from django.conf.urls import include, url

from .v1.urls import urlpatterns as v1_urls

urlpatterns = [
    url(r'^v1/', include((v1_urls, 'v1'), namespace='v1'))
]