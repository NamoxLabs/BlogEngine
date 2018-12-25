from django.utils.functional import SimpleLazyObject

from rest_framework import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError

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
            post_obj = PModel.objects.create(**validated_data)
            return post_obj