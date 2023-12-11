from rest_framework import serializers
from .models import Invest


class InvestSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    old_price = serializers.FloatField(required=True)
    new_price = serializers.FloatField(required=True)
    growth = serializers.FloatField(required=True)
    recommendations = serializers.CharField(required=True, allow_blank=False, max_length=200)

    def create(self, validated_data):
        return Invest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.old_price = validated_data.get('old_price', instance.old_price)
        instance.new_price = validated_data.get('new_price', instance.new_price)
        instance.growth = validated_data.get('growth', instance.growth)
        instance.recommendations = validated_data.get('recommendations', instance.recommendations)
        instance.save()
        return instance
