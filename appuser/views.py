
# appuser/views.py

from rest_framework import viewsets
from .models import AppUser
from .serializers import AppUserSerializer

class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer