from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from test_api.account.views import LoginView, LogoutView, RegisterView


class OptionalSlashRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/register/', RegisterView.as_view(), name='register-view'),
    path('api/v1/login', LoginView.as_view(), name='login-view'),
    path('api/v1/logout', LogoutView.as_view(), name='logout-view'),
]
