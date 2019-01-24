from django.utils.functional import SimpleLazyObject

from rest_framework import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError

from engine.hashtag.models import Hashtag as HashModel
from engine.category.models import Category as CModel, Subcategory as SBModel
from engine.post.models import Post as PModel

from engine.hashtag.serializers import HashSerializer
from engine.category.serializers import CSerializer, SBSerializer

from engine.utils import get_request_token


class PSerializer(serializers.ModelSerializer):
    category = CSerializer(many=False, read_only=True)
    subcategories = SBSerializer(many=True, read_only=True)
    hashtags = HashSerializer(many=True, read_only=True)

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
            unvalidated_data = self.context['request'].data
            print("unvalidated_data")
            print(unvalidated_data)
            category = unvalidated_data.get('category')
            print("category")
            print(category)
            category_obj = CModel.objects.get(pk=category)
            validated_data['category'] =  category_obj
            print("validated_data")
            print(validated_data)
            #subcategories = unvalidated_data.get('subcategories', [])
            subcategories = unvalidated_data.pop('subcategories')
            print("subcategories")
            print(subcategories)
            hashtags = unvalidated_data.pop('hashtags')
            print("hashtags")
            print(hashtags)
            post_obj = PModel.objects.create(**validated_data)
            if post_obj is not None:
                post_obj.hashtags.set(hashtags)
                for subcategory in subcategories:
                    print("subcategory")
                    print(subcategory)
                    subcategory_obj = SBModel.objects.get(pk=subcategory)
                    post_obj.subcategories.add(subcategory_obj)
                    # post_obj.subcategories.set(subcategory_obj)
                for hashtag in hashtags:
                    print("hashtag")
                    print(hashtag)
                    hashtag_obj = HashModel.objects.get(name=hashtag)
                    if hashtag_obj is None:
                        hashtag_obj = HashModel.objects.create(name=hashtag)
                    post_obj.hashtags.add(hashtag_obj)
            return post_obj
