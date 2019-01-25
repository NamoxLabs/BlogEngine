from rest_framework import serializers


class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = PModel
        fields = ('id', 'created_by', 'created_at', 'changed', 'active')