from django.utils.functional import SimpleLazyObject

from rest_framework import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError

from engine.category.models import Category as CModel, Subcategory as SBModel

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


class SBSerializer(serializers.ModelSerializer):
    category = CSerializer(many=False, read_only=True)

    class Meta:
        model = SBModel
        fields = ('id', 'name', 'category', 'description', 'created_by', 
            'created_at', 'active',)

    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            unvalidated_data = self.context['request'].data
            category = unvalidated_data.get('category')
            category_obj = CModel.objects.get(pk=category)
            validated_data['category'] =  category_obj
            subcategory_obj = SBModel.objects.create(**validated_data)
            return subcategory_obj
