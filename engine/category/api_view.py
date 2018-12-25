# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login

from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework_jwt.settings import api_settings

from engine.category.models import Category as CModel, Subcategory as SBModel
from .serializers import CSerializer, SBSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'category': reverse('category-list', request=request, format=format),
        'subcategory': reverse('subcategory-list', request=request, format=format),
    })


class Categories(viewsets.ModelViewSet):
    queryset = CModel.objects.all()
    serializer_class = CSerializer
    permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save()


class Subcategories(viewsets.ModelViewSet):
    queryset = SBModel.objects.all()
    serializer_class = SBSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()