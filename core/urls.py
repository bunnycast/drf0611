from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from users.views import UserViewSet
from rest_framework.authtoken import views

router = SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'api-token-auth/', views.obtain_auth_token),
]
urlpatterns += router.urls


