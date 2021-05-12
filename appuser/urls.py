from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AppUserViewSet

router = SimpleRouter()
router.register('appuser', AppUserViewSet, basename="appuser")
urlpatterns = router.urls
