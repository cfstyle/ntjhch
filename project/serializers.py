#coding=utf-8
from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import (
        Project,
        ProjectApproval,
        ProjectAttachment,
        ProjectComment,
        Record,
        WorkType,
        WorkProcess,
        WorkAttachment,
        WorkRole,
        Work,
        WorkPerson
    )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    project_status_name = serializers.SerializerMethodField()
    tender_status_name = serializers.SerializerMethodField()
    contract_status_name = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    manager_name = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_project_status_name(self, obj):
        return obj.get_project_status_display()
    def get_tender_status_name(self, obj):
        return obj.get_tender_status_display()
    def get_contract_status_name(self, obj):
        return obj.get_contract_status_display()
    def get_manager_name(self, obj):
        return obj.manager.last_name + obj.manager.first_name

class ProjectApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectApproval
        fields = '__all__'

class ProjectAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAttachment
        fields = '__all__'

class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectComment
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = '__all__'

class WorkProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkProcess
        fields = '__all__'

class WorkAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkAttachment
        fields = '__all__'

class WorkRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkRole
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class WorkPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPerson
        fields = '__all__'