from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET',])
def collection_list(request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)
@api_view(['GET',])
def get_events(request,id):
    events =  Events.objects.filter(collection_id=id)
    serializer = EventsSerializer(events, many=True)
    return Response(serializer.data)