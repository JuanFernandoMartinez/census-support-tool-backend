from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class SaludoViewSet(ViewSet):
    def list(self, request):
        return Response({"mensaje": "hola"}, status=status.HTTP_200_OK)

    def create(self, request):
        return Response({"mensaje": "bien"}, status=status.HTTP_200_OK)

