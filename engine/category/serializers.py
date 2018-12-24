from django.utils.functional import SimpleLazyObject

from rest_framework import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError

from engine.category.models import Category as CModel


class CSerializer(serializers.ModelSerializer):
    class Meta:
        model = CModel
        fields = ('id', 'name', 'description', 'created_by', 
            'created_at', 'active',)

    def create(self, validated_data):
        token = self.context['request'].META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        data = {'token': token}
        try:
            user_data = VerifyJSONWebTokenSerializer().validate(data)
            user = user_data['user']
            validated_data['created_by'] = user
            category = CModel.objects.create(**validated_data)
            print("category")
            print(category)
            #category.add(created_by=user)
            return category
        except ValidationError as v:
            return
            #return Object
