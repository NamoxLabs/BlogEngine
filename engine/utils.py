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
