from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.permissions import IsOwner
from users.serializers import UserSerializer
from django.contrib.auth.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action == 'create':     # create는 로그인 없이도 가능
            return [AllowAny()]
        elif self.action in ['update', 'destroy']:      # update와 destroy는 자기가 등록한 것만 가능
            return [IsOwner()]

        return super().get_permissions()

    @method_decorator(cache_page(60 * 60 * 2))      # caching을 위한 데코레이터 세팅
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    def rertrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
