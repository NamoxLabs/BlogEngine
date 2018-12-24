from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from engine.account import api_view as users_api
from engine.category import api_view as category_api
#from engine.subcategory import api_view as subcategory_api
#from engine.post import api_view as post_api

router = DefaultRouter()
#router.register(r'category', category_api.Category)

urlpatterns = [
    #path('auth/register/', users_api.RegisterUsers.as_view(), name='auth-register'),
    #path('auth/login/', users_api.LoginView.as_view(), name='auth-login'),
    url(r'^api-token-auth/', obtain_jwt_token, name='create-token'),
    url(r'^api-token-refresh/', refresh_jwt_token, name='refresh-token'),
    url(r'^api-token-verify/', verify_jwt_token, name='verify-token'),
    path('', include(router.urls)),
]
