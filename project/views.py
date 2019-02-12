#encoding=utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action, list_route
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
from project.serializers import (
        UserSerializer,
        ProjectSerializer,
        ProjectApprovalSerializer,
        ProjectAttachmentSerializer,
        ProjectCommentSerializer,
        RecordSerializer,
        WorkTypeSerializer,
        WorkProcessSerializer,
        WorkAttachmentSerializer,
        WorkRoleSerializer,
        WorkSerializer,
        WorkPersonSerializer
    )
import os
from ntjhch.settings import FILE_UPLOAD_PATH
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['post'], detail=True)
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def recent_users(self, request):
        recent_users = User.objects.all().order('-last_login')

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    @list_route(methods=['get'])
    def pending(self, request):
        '''
        待审批项目
        '''
        queryset = Project.objects.filter(project_status=0)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializers.data)

    @list_route(methods=['post'])
    def reject(self, request):
        '''
        审批驳回
        '''
        rs = { 'flag': True, 'info': ''}
        project = request.data.get('projectId')
        if project:
            Project.objects.filter(id=project).update(project_status=4)
        else:
            rs['flag'] = False
            rs['info'] = 'projectId can not be null.'
        return Response(rs)

    @list_route(methods=['post'])
    def accept(self, request):
        '''
        审批通过
        '''
        rs = { 'flag': True, 'info': ''}
        project = request.data.get('projectId')
        if project:
            Project.objects.filter(id=project).update(project_status=1)
        else:
            rs['flag'] = False
            rs['info'] = 'projectId can not be null.'
        return Response(rs)

class ProjectApprovalViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectApprovalSerializer
    queryset = ProjectApproval.objects.all()

class ProjectAttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectAttachmentSerializer
    queryset = ProjectAttachment.objects.all()

    @list_route(methods=['post'])
    def upload(self, request):
        '''
        上传文件
        '''
        rs = {
            'flag': True,
            'info': ''
        }
        project = request.POST.get('project')
        files = request.FILES.getlist('file')
        category = request.POST.get('category')
        for file in files:
            filename = file.name
            try:
                pa = ProjectAttachment()
                pa.project = Project.objects.get(id=project)
                pa.category = category
                pa.user = request.user
                pa.name = file
                pa.save()
            except Exception as e:
                rs['flag'] = False
                rs['info'] += u'{} 上传失败！{}'.format(filename, e.message)
        return Response(rs)

class ProjectCommentViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectCommentSerializer
    queryset = ProjectComment.objects.all()

class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()

class WorkTypeViewSet(viewsets.ModelViewSet):
    serializer_class = WorkTypeSerializer
    queryset = WorkType.objects.all()

class WorkProcessViewSet(viewsets.ModelViewSet):
    serializer_class = WorkProcessSerializer
    queryset = WorkProcess.objects.all()

class WorkAttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = WorkAttachmentSerializer
    queryset = WorkAttachment.objects.all()

class WorkRoleViewSet(viewsets.ModelViewSet):
    serializer_class = WorkRoleSerializer
    queryset = WorkRole.objects.all()

class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()

class WorkPersonViewSet(viewsets.ModelViewSet):
    serializer_class = WorkPersonSerializer
    queryset = WorkPerson.objects.all()

