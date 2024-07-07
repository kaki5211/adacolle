# from .views import VideoCreateView, VideoAPIView
from rest_framework import routers
from .views import VideoViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet, basename='video')
# router.register(r'entries', VideoAPIView)
