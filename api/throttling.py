from rest_framework.throttling import SimpleRateThrottle

from api.models import User


class MyThrottling(SimpleRateThrottle):
    scope = 'user'
    def get_cache_key(self, request, view):
        # return request.META.get('REMOTE_ADDR')
        return request.data.get('username')