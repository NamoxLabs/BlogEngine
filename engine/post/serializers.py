from django.utils.functional import SimpleLazyObject

from rest_framework import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError

from engine.hashtag.models import Hashtag as HashModel
from engine.category.models import Category as CModel, Subcategory as SBModel
from engine.post.models import Post as PModel

from engine.utils import get_request_token


class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = PModel
        fields = ('id', 'name', 'content', 'category',
            'subcategories', 'hashtags', 'created_by', 'created_at',
            'changed', 'active')
    
    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            unvalidated_data = self.context['request'].data
            category = unvalidated_data.get('category')
            category_obj = CModel.objects.get(pk=category)
            validated_data['category'] =  category_obj
            subcategories = unvalidated_data.get('subcategories', [])
            hashtags = validated_data.pop('hashtags')
            post_obj = PModel.objects.create(**validated_data)
            if post_obj is not None:
                post_obj.hashtags.set(hashtags)
            return post_obj
