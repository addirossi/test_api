from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from test_api.core.models import AppModel
from test_api.core.serializers import AppSerializer


class AppViewSet(viewsets.GenericViewSet,
                 CreateModelMixin,
                 ListModelMixin,
                 UpdateModelMixin,
                 DestroyModelMixin):
    queryset = AppModel.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request}

    @action(['POST'], detail=True)
    def create_api_key(self, request, pk=None):
        app = self.get_object()
        app.generate_api_key()
        return Response(app.API_KEY)


class APITestView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        API_KEY = request.META.get('HTTP_API_KEY')
        print(request.META)
        app = get_object_or_404(AppModel.objects.all(), API_KEY=API_KEY)
        serializer = AppSerializer(instance=app)
        return JsonResponse(data=serializer.data)

