from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework_jwt.settings import api_settings

from engine.post.models import Post as PModel
from .serializers import PSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'post': reverse('post-list', request=request, format=format),
    })


class Post(viewsets.ModelViewSet):
    queryset = PModel.objects.all()
    serializer_class = PSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()