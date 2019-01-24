from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework_jwt.settings import api_settings

from engine.hashtag.models import Hashtag as HashModel
from .serializers import HashSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'hashtag': reverse('hashtag-list', request=request, format=format),
    })

class Hashtag(viewsets.ModelViewSet):
    queryset = HashModel.objects.all()
    serializer_class = HashSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()