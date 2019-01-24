from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

def get_request_token(func):
    def func_wrapper(self, validated_data):
        token = self.context['request'].META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        data = {'token': token}
        user_data = VerifyJSONWebTokenSerializer().validate(data)
        if user_data['user'] is not None:
            validated_data['created_by'] = user_data['user']
        else:
            validated_data['created_by'] = None
        obj_result = func(self, validated_data)
        return obj_result
    return func_wrapper


def get_user_token(func):
    def func_wrapper(self, request, pk=None):
        token = self.context['request'].META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        print("token")
        print(token)
        data = {'token': token}
        print("data")
        print(data)
        user_data = VerifyJSONWebTokenSerializer().validate(data)
        print("user_data")
        print(user_data)
        if user_data['user'] is not None:
            validated_data['created_by'] = user_data['user']
        else:
            validated_data['created_by'] = None
        obj_result = wrapped(self, request, pk)
        print("obj_result")
        print(obj_result)
        return obj_result
    return func_wrapper

"""
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

#upload to digital ocean