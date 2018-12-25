from django.utils.functional import SimpleLazyObject

from rest_framework import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError

from engine.category.models import Category as CModel

from engine.utils import get_request_token


class CSerializer(serializers.ModelSerializer):
    class Meta:
        model = CModel
        fields = ('id', 'name', 'description', 'created_by', 
            'created_at', 'active',)


    @get_request_token
    def create(self, validated_data):
        print("validated_data")
        print(validated_data)
        #token = self.context['request'].META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        #data = {'token': token}
        #try:
            #user_data = VerifyJSONWebTokenSerializer().validate(data)
            #user = user_data['user']
            #validated_data['created_by'] = user
        if validated_data['created_by']:
            category_obj = CModel.objects.create(**validated_data)
            print("category_obj")
            print(category_obj)
            #category.add(created_by=user)
            return category_obj
            
        #except ValidationError as v:
        #    return
            #return Object
