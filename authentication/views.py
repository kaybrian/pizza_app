from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response


class HelloAuthView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={
            "Message": "Hello, Welcome to the platform"
        }, status=status.HTTP_200_OK)