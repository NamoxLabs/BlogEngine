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
#Admin default modules
from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from engine.multimedia import api_view as multimedia_api
from engine.account import api_view as users_api
from engine.category import api_view as category_api
from engine.post import api_view as post_api
from engine.hashtag import api_view as hash_api

router = DefaultRouter()
router.register(r'hashtags', hash_api.Hashtag)
router.register(r'categories', category_api.Categories)
router.register(r'subcategories', category_api.Subcategories)
#router.register(r'multimedia', multimedia_api.MultimediaHandler)
router.register(r'multimedia/user', multimedia_api.MultimediaUser)
router.register(r'multimedia/category', multimedia_api.MultimediaCategory)
router.register(r'multimedia/subcategory', multimedia_api.MultimediaSubcategory)
router.register(r'multimedia/post', multimedia_api.MultimediaPost)
router.register(r'posts', post_api.DataPost)
#router.register(r'create/posts', post_view.Post.as_view())

from engine.multimedia import api_view as multimedia_view
from engine.post import api_view as post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', users_api.RegisterUsers.as_view(), name='auth-register'),
    #url(r'^create-multimedia/', multimedia_view.MultimediaHandler.as_view(), name='create-multimedia'),
    #url(r'^create-post/', post_view.Post.as_view(), name='create-post'),
    url(r'^api-token-auth/', obtain_jwt_token, name='create-token'),
    url(r'^api-token-refresh/', refresh_jwt_token, name='refresh-token'),
    url(r'^api-token-verify/', verify_jwt_token, name='verify-token'),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
