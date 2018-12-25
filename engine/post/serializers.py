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
            print("validated_data")
            print(validated_data)
            print("self.context['request'].data")
            print(self.context['request'].data)
            unvalidated_data = self.context['request'].data
            print("unvalidated_data")
            print(unvalidated_data)
            category = unvalidated_data.get('category')
            print("category")
            print(category)
            category_obj = CModel.objects.get(pk=category)
            print("category_obj")
            print(category_obj)
            validated_data['category'] =  category_obj
            subcategories = unvalidated_data.get('subcategories', [])
            print("subcategories")
            print(subcategories)
            hashtags = unvalidated_data.get('hashtags', [])
            print("hashtags")
            print(hashtags)
            if hashtags is not None:
                for hashtag in hashtags:
                    HashModel.objects.get()
            post_obj = PModel.objects.create(**validated_data)
            if post_obj is not None:
                for subcategory in subcategories:
                    post_obj.subcategories.add(subcategory)
                for hashtag in hashtags:
                    post_obj.hashtags.add(hashtag)
            return post_obj
