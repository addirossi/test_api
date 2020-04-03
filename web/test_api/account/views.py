from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, exceptions, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import LoginForm
from .serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(_('Successfully registered'), status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        user, token = LoginForm(request.data).save()
        serializer = UserSerializer(user, context={'request': request})
        result = serializer.data
        result['token'] = token
        return Response(result)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            logout(request)
        except Token.DoesNotExist:
            raise exceptions.NotFound(_('User is not signed in'))
        return Response({"detail": _("Successfully logged out.")})