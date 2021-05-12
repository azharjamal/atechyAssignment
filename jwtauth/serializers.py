from django.db import models
from rest_framework import serializers
from appuser.models import AppUser

User =  AppUser 


class UserLoginSerializer(serializers.ModelSerializer):
    emailaddress = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AppUser
        fields = [
            "emailaddress",
            "password",
            "role",
        ]

