from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.throttling import BaseThrottle, UserRateThrottle
from api import models
from django.contrib.auth.models import Group, Permission
from rest_framework.request import Request

# Create your views here.
from api.throttling import MyThrottling


class demo_1(APIView):
    throttle_classes = [MyThrottling]
    def get(self,request,*args,**kwargs):
        return Response('读操作')

    def post(self,request,*args,**kwargs):
        return Response('写操作')

class demo_2(APIView):
    pass