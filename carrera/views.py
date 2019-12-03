from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from carrera.models import Carrera
from carrera.serializer import CarreraSerializers
from rest_framework.request import Request
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)

class CarreraList(APIView):

    def get(self, request):
        queryset = Carrera.objects
        serializer = CarreraSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CarreraSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class CarreraDetail(APIView):
    def get_object(self, id):
        try:
            return Carrera.objects.get(pk=id)
        except Carrera.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        carrera = self.get_object(id)
        if carrera != 404:
            serializer = CarreraSerializers(carrera)
            return Response(serializer.data)
        else:
            return Response(carrera)

    def put(self, request, id, format=None):
        carrera = self.get_object(id)
        if carrera != 404:
            serializer = CarreraSerializers(carrera, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(carrera, status = HTTP_400_BAD_REQUEST)

    def delete(self,request,id, format=None):
        carrera = self.get_object(id)
        if carrera != 404:
            carrera.delete()
        return Response(status=HTTP_204_NO_CONTENT)