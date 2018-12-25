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
        if validated_data['created_by']:
            category_obj = CModel.objects.create(**validated_data)
            return category_obj
