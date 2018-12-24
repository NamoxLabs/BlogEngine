from rest_framework import serializers
from .models import Category

class CSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_by', 
            'created_at', 'active')