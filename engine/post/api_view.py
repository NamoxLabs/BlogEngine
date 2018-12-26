from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from engine.post.models import Post as PModel
from .serializers import PSerializer

from engine.utils import get_request_token, get_user_token


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
    authentication_classes = (JSONWebTokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    """
    @detail_route(
        mmethods = ['post', 'put', 'patch', 'get'],
        permission_classes = [permissions.IsAuthenticated],
        authentication_classes = [JSONWebTokenAuthentication],
        serializer_class = MultimediaSerializer,
    )
    """
    @get_user_token
    def create_post(self, request, pk=None):
        print("l")

    """
    def perform_create(self, serializer):
        serializer.save()
    """
