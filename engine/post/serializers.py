import json
import ast

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
            #print("validated_data")
            #print(validated_data)
            unvalidated_data = self.context['request'].data
            print("unvalidated_data")
            print(unvalidated_data)
            category = unvalidated_data.get('category')
            category_obj = CModel.objects.get(pk=category)
            validated_data['category'] =  category_obj
            print("validated_data")
            print(validated_data)
            #subcategories = unvalidated_data.pop('subcategories')
            subcategories = unvalidated_data.get('subcategories')
            print("subcategories")
            print(subcategories)
            print(type(subcategories))
            #hashtags = unvalidated_data.pop('hashtags')
            hashtags = unvalidated_data.get('hashtags')
            print("hashtags")
            print(hashtags)
            post_obj = PModel.objects.create(**validated_data)
            if post_obj is not None:
                subcategory_list = subcategories.split(', ')
                print("subcategory_list")
                print(subcategory_list)
                subcategories_list = ast.literal_eval(subcategories)
                print("subcategories_list")
                print(subcategories_list)
                for subcategory in subcategories_list:
                    print("subcategory")
                    print(subcategory)
                    #print("subcategory list")
                    #print(json.loads(subcategories_list))
                    #for subcategory in subcategories_list:
                    #    print("subcategory")
                    #    print(subcategory)
                    try:
                        # This line is generating error because record doesn't exists[1]
                        subcategory_obj = SBModel.objects.get(pk=int(subcategory))
                    except SBModel.DoesNotExist:
                        subcategory_obj = None
                    if subcategory_obj is not None:
                        post_obj.subcategories.add(subcategory_obj)
                hashtags_list = ast.literal_eval(hashtags)
                print("hashtags_list")
                print(hashtags_list)
                for hashtag in hashtags_list:
                    print("hashtag")
                    print(hashtag)
                    try:
                        # This line is generating error because record doesn't exists[1]
                        hashtags_obj = HashModel.objects.get(name=str(subcategory))
                    except HashModel.DoesNotExist:
                        print("validated_data User")
                        print(validated_data.created_by)
                        hashtags_obj = HashModel.objects.create(name=str(subcategory))
                        #hashtags_obj = None
                    print("hashtags_obj")
                    print(hashtags_obj)
                    if hashtags_obj is not None:
                        post_obj.hashtags.add(hashtags_obj)
                return post_obj
