from rest_framework import serializers

from test_api.core.models import AppModel


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppModel
        fields = ('APP_ID', 'name', 'description')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['API_KEY'] = instance.API_KEY
        return representation
