from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
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

class ProjectApprovalViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectApprovalSerializer
    queryset = ProjectApproval.objects.all()

class ProjectAttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectAttachmentSerializer
    queryset = ProjectAttachment.objects.all()

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

