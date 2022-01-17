from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from home.models import OurModel
from home.serializers import OurModelSerializer


@api_view(['GET'])
def my_view(request):
    our_model = OurModel.objects.all()
    serializer = OurModelSerializer(our_model, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_view(request):
    our_model = OurModelSerializer(data=request.data)
    if our_model.is_valid():
        our_model.save()
        return Response(our_model.data, status=status.HTTP_201_CREATED)
    return Response(our_model.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detail_view(request, pk):
    # try:
    #     our_model = OurModel.objects.get(pk=pk)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    our_model = get_object_or_404(OurModel, pk=pk)
    if request.method == 'GET':
        serializer = OurModelSerializer(our_model)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        partial = request.method == 'PATCH'
        serializer = OurModelSerializer(our_model, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        our_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def next_view(request):
    if request.method == 'GET':
        return Response('method Get')
    else:
        return Response(request.data, status=status.HTTP_201_CREATED)



