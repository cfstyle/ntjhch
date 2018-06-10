#coding=utf-8
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        if 'username' not in request.data.keys():
            data = request.data
            data.update({
                'username': data.get('userName')
                })
        serializer = self.serializer_class(data=data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'code': 200,
            'token': 'Token ' + token.key,
            'user_id': user.pk,
            'avator': '',
            'user_name': user.username, 
            'access': [],
            'email': user.email
        })