from django.shortcuts import render
from filemanage.models import (
        File,
    )
from filemanage.serializers import (
        FileSerializer,
    )
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action, list_route

# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()