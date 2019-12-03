from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from registro.models import Registro
from registro.serializer import RegistroSerializers

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
import json

class RegistroList(APIView):

    def get(self, request, format=None):
        queryset = Registro.objects
        serializer = RegistroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        received_json_data=json.loads(request.body)
        

        print(received_json_data)
        datos = {'name':received_json_data["name"], 'lastname':received_json_data["lastname"],'age':received_json_data["age"], 'gender':received_json_data["gender"], 'address':received_json_data["address"],  'carrera':received_json_data["carrera"]}
        serializer = RegistroSerializers(data=datos)
        if serializer.is_valid():
            serializer.save()
            datasx = serializer.data
            return Response(datasx)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RegistroDetail(APIView):
    def get_object(self, id):
        try:
            return Registro.objects.get(pk=id)
        except Registro.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        registro = self.get_object(id)
        if registro != 404:
            serializer = RegistroSerializers(registro)
            return Response(serializer.data)
        else:
            return Response(registro)

    def put(self, request, id, format=None):
        registro = self.get_object(id)
        received_json_data=json.loads(request.body)
        datos = {'name':received_json_data["name"], 'lastname':received_json_data["lastname"],'age':received_json_data["age"], 'gender':received_json_data["gender"], 'address':received_json_data["address"],  'carrera':received_json_data["carrera"]}
        if registro != 404:
            serializer = RegistroSerializers(registro, data=datos)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(registro, status = HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id, format=None):
        registro = self.get_object(id)
        if registro != 404:
            registro.delete()
        return Response(status=HTTP_204_NO_CONTENT)