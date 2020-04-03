from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, min_length=6, write_only=True)
    password_confirmation = serializers.CharField(required=True, write_only=True, min_length=6)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'password_confirmation',
            'first_name',
            'last_name',
        )

    def validate(self, data):
        password = data['password']
        password_confirm = data['password_confirmation']
        if password != password_confirm:
            raise serializers.ValidationError(_('Wrong password confirmation'))
        return data

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        user.is_active = True
        user.save()
        return user

    def to_representation(self, instance):
        representation = super(UserSerializer, self).\
            to_representation(instance)
        return representation
