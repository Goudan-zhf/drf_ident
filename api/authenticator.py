from rest_framework import authentication, exceptions
from rest_framework.authentication import BaseAuthentication

from api.models import User


class MyAuth(BaseAuthentication):

    def authenticate(self, request):
        auth = request.META.get("HTTP_AUTHORIZATION", None)

        if auth is None:
            return None

        auth_list = auth.split()

        if not (len(auth_list) == 2 and auth_list[0].lower() == "auth"):
            raise exceptions.APIException("用户认证信息格式有误")

        if auth_list[1] != "tom":
            raise exceptions.APIException("用户信息校验失败")
        username=request.data.get('username')

        user = User.objects.filter(username=username).first()

        if not user:
            raise exceptions.APIException("用户不存在")
        return (user, None)