#coding=utf-8
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import traceback
# Create your views here.
from django.conf import settings


def user_login(request):
    '''
    登录
    '''
    rs = {
        'code': 200,
        'msg': ''
    }
    username = request.POST.get('username', eval(request.body).get('userName'))
    password = request.POST.get('password', eval(request.body).get('password'))
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        rs['msg'] = u'登录成功'
    else:
        rs['code'] = 204
        rs['msg'] = u'用户名或密码错误！'
    return JsonResponse(rs)

def user_logout(request):
    '''
    注销
    '''
    rs = {
        'code': 200,
        'msg': ''
    }
    try:
        logout(request)
        rs['msg'] = 'logout success'
    except:
        traceback.print_exc()
        rs['msg'] = 'logout exception!'
    return JsonResponse(rs)

@api_view(['GET'])
def get_users(request):
    '''
    获取除admin的所有用户
    '''
    rs = {
        'code': 200,
        'msg': ''
    }
    try:
        
        users = User.objects.filter(is_superuser=0)
        rs['users'] = map(lambda x: {
                'id': x.id,
                'username': x.get_username(),
                'realname': x.last_name + x.first_name,
                # 'realname': x.get_full_name(),
                'groups': x.groups.values_list('name', flat=True),
                'role': min([settings.ROLE.get(each, 999) for each in x.groups.values_list('name', flat=True)])
            }, users)
    except:
        traceback.print_exc()
        rs['msg'] = 'get users faild.'
    return Response(rs)
