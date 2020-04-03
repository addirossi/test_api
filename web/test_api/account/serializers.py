from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
        )

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        user.is_active = True
        user.save()
        return user

    def to_representation(self, instance):
        representation = super(UserSerializer, self).\
            to_representation(instance)
        return representation
