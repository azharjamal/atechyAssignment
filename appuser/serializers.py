
from rest_framework import serializers
from .models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "firstname", "lastname", "emailaddress", "password", "role")
        model = AppUser