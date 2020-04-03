from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from test_api.account.views import LoginView, LogoutView, RegisterView
from test_api.core.views import AppViewSet, APITestView


class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register('app', AppViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('login', LoginView.as_view(), name='login-view'),
    path('logout', LogoutView.as_view(), name='logout-view'),
    path('api/test/', APITestView.as_view(), name='app-test')
]
