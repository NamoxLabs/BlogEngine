from rest_framework import generics, permissions, renderers, viewsets, authentication
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework_jwt.settings import api_settings

from engine.multimedia.models import MultimediaUser as MulUserModel, MultimediaCategory as MulCatModel,\
    MultimediaSubategory as MulSubCModel, MultimediaPost as MulPostModel
from .serializers import MulUserSerializer, MulCatSerializer,\
    MulSubCSerializer, MulPostSerializer

from engine.utils import get_request_token, get_user_token

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'multimedia': reverse('multimedia-list', request=request, format=format),
    })


class MultimediaHandler(APIView):
    #authentication_classes = (authentication.JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    #permission_classes = (permissions.IsAdminUser,)

    def post(self, request, format=None):
        print("request.FILES")
        print(request.FILES)
        request.FILES
        #serializer = UserAvatarSerializer(files=request.FILES)
        #print("serializer")
        #print(serializer)
        if serializer.is_valid():
            print("funca")
            serializer.save()
            return Response(serializer.data)
"""
class MultimediaHandler(viewsets.ModelViewSet):
    queryset = MulUserModel.objects.all()
    serializer_class = UserAvatarSerializer
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,)
    
    @get_user_token
    #@get_multimedia
    #def create_img(self, request, pk=None):
    def create_img(self, obj):
        print("l")
        obj.temp_file = self.request.FILES.get('image')
        print("obj")
        print(obj)
"""


class MultimediaUser(viewsets.ModelViewSet):
    queryset = MulUserModel.objects.all()
    serializer_class = MulUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @get_user_token
    #@get_multimedia
    def create_post(self, request, pk=None):
        print("l")


class MultimediaCategory(viewsets.ModelViewSet):
    queryset = MulCatModel.objects.all()
    serializer_class = MulCatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


class MultimediaSubcategory(viewsets.ModelViewSet):
    queryset = MulSubCModel.objects.all()
    serializer_class = MulSubCSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


class MultimediaPost(viewsets.ModelViewSet):
    queryset = MulPostModel.objects.all()
    serializer_class = MulPostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()