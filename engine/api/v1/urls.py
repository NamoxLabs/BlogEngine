from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token,/
    verify_jwt_token

from .users import api as users_api
from .category import api as category_api
from .subcategory import api as subcategory_api
from .post import api as post_api

router = DefaultRouter()
router.register(r'category', category_api.Category)

urlpatterns = [
    path('auth/register/', users_api.RegisterUsers.as_view(), name='auth-register'),
    path('auth/login/', users_api.LoginView.as_view(), name='auth-login'),
    url(r'^api-token-auth/', obtain_jwt_token, name='create-token'),
    url(r'^api-token-refresh/', refresh_jwt_token, name='refresh-token'),
    url(r'^api-token-verify/', verify_jwt_token, name='verify-token'),
    path('', include(router.urls)),
]
