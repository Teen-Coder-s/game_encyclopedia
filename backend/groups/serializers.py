from rest_framework import serializers
from .models import *

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    collection_id = serializers.IntegerField()
    name = serializers.CharField(required=True,max_length=100)
    description = serializers.CharField(max_length=None)
    image = serializers.ImageField(use_url='collection_images/')
    color = serializers.CharField(required=True,max_length=100)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Collection` instance, given the validated data.
        """
        return collection.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Collection` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.color = validated_data.get('color', instance.color)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance

class EventsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    collection_id = serializers.IntegerField()
    title = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(max_length=None)
    image = serializers.ImageField(use_url='events_images/')
    event_at = serializers.DateTimeField()

class ArticlesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    collection_id = serializers.IntegerField()
    title = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(max_length=None)
    image = serializers.ImageField(use_url='articles_images/')