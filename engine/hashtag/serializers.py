from django.utils.functional import SimpleLazyObject

from rest_framework import serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError

from engine.hashtag.models import Hashtag as HashModel

from engine.utils import get_request_token


class HashSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashModel
        fields = ('id', 'name', 'content', 'created_by', 'created_at',
            'changed', 'active')
    
    @get_request_token
    def create(self, validated_data):
        if validated_data['created_by']:
            unvalidated_data = self.context['request'].data
            print("unvalidated_data")
            print(unvalidated_data)
            hashtag = unvalidated_data.get('name')
            print("hashtag")
            print(hashtag)
            hashtag_prev = HashModel.objects.all(name=hashtag)
            print("hashtag_prev")
            print(hashtag_prev)
            if hashtag_prev is not None:
                return hashtag_prev
            else:
                hashtag_obj = HashModel.objects.create(**validated_data)
                return hashtag_obj
