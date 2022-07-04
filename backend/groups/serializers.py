from rest_framework import serializers
from .models import *

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
class FactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facts
        fields = '__all__'