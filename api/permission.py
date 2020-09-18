from rest_framework.permissions import BasePermission

from api.models import User


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        # 如果是只读接口  则所有人都可以访问
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        username = request.data.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            return True
        return False
