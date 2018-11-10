"""engine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .account.urls import urlpatterns as account_urls
from .core.sitemaps import sitemaps
from .core.urls import urlpatterns as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(core_urls)),
    url(r'^category/', include((category_urls, 'category'), namespace='category')]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        # static files (images, css, javascript, etc.)
        url(r'^static/(?P<path>.*)$', serve)] + static(
            '/media/', document_root=settings.MEDIA_ROOT
        )