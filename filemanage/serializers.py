#coding=utf-8
from rest_framework import serializers
from django.contrib.auth.models import User
from filemanage.models import (
        File
    )

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

