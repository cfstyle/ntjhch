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
from django.contrib import admin
from rest_framework.authtoken import views
from .authtoken import CustomAuthToken
from django.views.static import serve
from ntjhch.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/project/', include('project.urls')),
    url(r'^api/fm/', include('filemanage.urls')),
    #url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-token-auth/', CustomAuthToken.as_view()),
    url(r'^api/user/', include('user.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT})
]
