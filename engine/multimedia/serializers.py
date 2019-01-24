from django.utils.functional import SimpleLazyObject

from rest_framework import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError

from engine.multimedia.models import MultimediaUser as MulUserModel, MultimediaCategory as MulCatModel,\
    MultimediaSubategory as MulSubCModel, MultimediaPost as MulPostModel
from engine.utils import get_request_token


class MulUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MulUserModel
        fields = ('id', 'name', 'content', 'user_related',
            'created_by', 'created_at', 'changed', 'active')
    
    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            multimedia_user_obj = MulUserModel.objects.create(**validated_data)
            return multimedia_user_obj


class MulCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MulCatModel
        fields = ('id', 'name', 'content', 'category',
            'created_by', 'created_at', 'changed', 'active')
    
    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            multimedia_cat_obj = MulCatModel.objects.create(**validated_data)
            return multimedia_cat_obj


class MulSubCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MulSubCModel
        fields = ('id', 'name', 'content', 'subcategory',
            'created_by', 'created_at', 'changed', 'active')
    
    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            multimedia_sub_obj = MulSubCModel.objects.create(**validated_data)
            return multimedia_sub_obj


class MulPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MulPostModel
        fields = ('id', 'name', 'content', 'post',
            'created_by', 'created_at', 'changed', 'active')
    
    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            multimedia_post_obj = MulPostModel.objects.create(**validated_data)
            return multimedia_post_obj
