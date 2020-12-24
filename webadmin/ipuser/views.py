from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import IPUser
from .serializers import IPUserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics

import csv
from django.http import HttpResponse

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics


# @api_view(['GET', ])
# def download_ip_user(request):
#     data = IPUser.objects.all()
#     serializer = IPUserSerializer(data, many=True)
#
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="ipuser.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['id', 'user', 'ip_addr', 'mac_addr'])
#     for i in serializer.data:
#         writer.writerow([i['id'], i['user'], i['ip_addr'], i['mac_addr']])
#     return response
#
#
# @extend_schema(request=IPUserSerializer, responses={201: IPUserSerializer})
# @api_view(['POST', ])
# def ip_user(request):
#     serializer = IPUserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)

# from functools import wraps
# from .urls import urlpatterns
# from django.urls import path
# from django.conf.urls import url
#
# def add_url(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         urlpatterns.append(path('ipuser/', fn),)
#         return fn(*args, **kwargs)
#     return wrapper


class SnippetList(generics.ListCreateAPIView):
    queryset = IPUser.objects.all()
    serializer_class = IPUserSerializer

    @extend_schema(description='return ipuser.csv', responses={201: None})
    def get(self, request, *args, **kwargs):
        data = IPUser.objects.all()
        serializer = IPUserSerializer(data, many=True)

        response = HttpResponse()
        response['Content-Disposition'] = 'attachment; filename="ipuser.csv"'
        writer = csv.writer(response)
        writer.writerow(['id', 'user', 'ip_addr', 'mac_addr'])
        for i in serializer.data:
            writer.writerow([i['id'], i['user'], i['ip_addr'], i['mac_addr']])
        return response


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):#can
#     queryset = IPUser.objects.all()
#     serializer_class = IPUserSerializer


from rest_framework import viewsets
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = IPUser.objects.all()
    serializer_class = IPUserSerializer