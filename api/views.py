from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Bar, Special
from .serializers import BarSerializer, SpecialSerializer
# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
        'Endpoint': '/bars/',
        'method': 'GET',
        'body': None, 
        'description': 'return array of bars/restaurants'
        },
        {
        'Endpoint': '/bars/id',
        'method': 'GET',
        'body': None, 
        'description': 'return a single bar'
        },
        {
        'Endpoint': '/bars/create',
        'method': 'POST',
        'body': {'body': ""}, 
        'description': 'creates a new bar from a post request'
        },
        {
        'Endpoint': '/bars/id/update/',
        'method': 'PUT',
        'body': {'body': ""},
        'description': 'Creates an existing bar with data sent in post request'
        },
        {
        'Endpoint': '/bars/id/delete/',
        'method': 'DELETE',
        'body': None,
        'description': 'Deletes and exiting bar'
        },
        {
        'Endpoint': '/bars/id/special/create',
        'method': 'POST',
        'body': {'body': ""}, 
        'description': 'add a special to a bar'
        },
        {
        'Endpoint': '/specials/id',
        'method': 'GET',
        'body': None, 
        'description': 'return a single bar special'
        },
        {
        'Endpoint': '/bars/bar_id/specials/special_id/update',
        'method': 'PUT',
        'body': {'body': ""},
        'description': 'Creates an existing special with data sent in post request'
        },
         {
        'Endpoint': '/bars/bar_id/specials/special_id/delete',
        'method': 'DELETE',
        'body': None,
        'description': 'deletes a special'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getBars(request):
    bars = Bar.objects.all()
    serializer =BarSerializer(bars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBar(request, pk):
    bar = Bar.objects.get(id=pk)
    # specials = Special.objects.filter(bar = request)
    serializer =BarSerializer(bar, many=False)
    # specialSerializer = SpecialSerializer(specials, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def createBar(request):
    data = request.data
    bar = Bar.objects.create(
        name=data['name'],
        address=data['address'],
        hours=data['hours']
    )
    serializer = BarSerializer(bar, namy=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateBar(request, pk):
    data = request.data
    bar = Bar.objects.get(id=pk)
    serializer = BarSerializer(instance=bar, data=data)

    if serializer.is_valid():
       serializer.save()

    return Response(serializer.data) 

@api_view(['DELETE'])
def deleteBar(request, pk):
    bar = Bar.objects.get(id=pk)
    bar.delete()
    return Response("Bar Deleted")


@api_view(['POST'])
def createSpecial(request, pk):
    # name = request.data.get("name")
    # days = request.data.get("days")
    # details = request.data.get("details")
    data = request.data
    bar = Bar.objects.get(pk=pk)
    special = Special.objects.create(
        name=data["name"], 
        days=data["days"], 
        details=data["details"], 
        bar=bar)
    serializer = SpecialSerializer(special, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateSpecial(request, bar_pk, special_pk):
    data = request.data
    special = Special.objects.get(id=special_pk)
    serializer = SpecialSerializer(instance=special, data=data)

    if serializer.is_valid():
       serializer.save()

    return Response(serializer.data) 

@api_view(['GET'])
def viewSpecial(request, bar_pk, special_pk):
    data = request.data
    special = Special.objects.get(id=special_pk)
    serializer = SpecialSerializer(instance=special, data=data)
    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def deleteSpecial(request, bar_pk, special_pk):
    special = Special.objects.get(id=special_pk)
    special.delete()
    return Response("Special Deleted")