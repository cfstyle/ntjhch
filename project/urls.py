#coding=utf-8
"""ntjhch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
#from rest_framework import router
from rest_framework.routers import DefaultRouter 
from project.views import (
        UserViewSet,
        ProjectViewSet,
        ProjectApprovalViewSet,
        ProjectAttachmentViewSet,
        ProjectCommentViewSet,
        RecordViewSet,
        WorkTypeViewSet,
        WorkProcessViewSet,
        WorkAttachmentViewSet,
        WorkRoleViewSet,
        WorkViewSet,
        WorkPersonViewSet
    )

#router = routers.SimpleRouter()
router = DefaultRouter()
router.register(r'users', UserViewSet)                                  # 用户
router.register(r'projects', ProjectViewSet)                            # 项目 
router.register(r'projectapproval', ProjectApprovalViewSet)             # 项目审批
router.register(r'projectattachments', ProjectAttachmentViewSet)        # 项目附件
router.register(r'projectcomments', ProjectCommentViewSet)              # 项目评论
router.register(r'records', RecordViewSet)                              # 日志记录
router.register(r'worktypes', WorkTypeViewSet)                          # 任务类型
router.register(r'workprocess', WorkProcessViewSet)                     # 任务进度
router.register(r'workattachments', WorkAttachmentViewSet)              # 任务附件
router.register(r'workroles', WorkRoleViewSet)                          # 任务角色
router.register(r'works', WorkViewSet)                                  # 任务
router.register(r'workpersons', WorkPersonViewSet)                      # 任务人员
#urlpatterns = router.urls

urlpatterns = [
    url(r'', include(router.urls))
    # url(r'^api/project/', include('project.urls')),
    # url(r'', ),
]
