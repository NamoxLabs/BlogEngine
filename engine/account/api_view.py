from django.contrib.auth import authenticate, login
"""
Django REST Framework libs
"""
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework_jwt.settings import api_settings

from .models import User

from .serializers import TokenSerializer

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@api_view(['POST'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
    })

class RegisterUsers(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        name = request.data.get("name", "")
        lastname = request.data.get("lastname", "")
        username = request.data.get("username", "")
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        repassword = request.data.get("repassword", "")
        rol = request.data.get("rol", "")
        invitation_code = request.data.get("invitation_code", "")
        if password == repassword:
            if not name and not lastname and not email and not password:
                return Response(
                    data={
                        "message": "username, password and email is required to register a user"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            new_user = User.objects.create_user(
                name=name, lastname=lastname, username=username, email=email,
                password=password, invitation_code=invitation_code, 
                rol=rol, is_staff_meetcare=False, is_active=False
            )
            return Response(status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    """
    POST auth/login
    """
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = User.objects.get(username=username)
        if user is None:
            user = User.objects.get(email=email)
        if user is not None:
            user_logged = user.check_password(password)
            """
            user = authenticate(request, username=username, password=password)
            if user is None:
                user = authenticate(request, email=username, password=password)
            """
            if user_logged:
                # Logins saves the user´s ID in the session,
                # using Django´s session framework.
                login(request, user)
                serializer = TokenSerializer(data={
                    # using DRF JWT utility functions to generate a token
                    "token": jwt_encode_handler(
                        jwt_payload_handler(user)
                    )})
                print("serializer")
                print(serializer)
                serializer.is_valid()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
                return Response(status=status.HTTP_404_NOT_FOUND)
