from rest_framework.routers import DefaultRouter
from api.views import *

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('artistes', ArtisteViewSet, basename='artistes')
router.register('songs', SongViewSet, basename='songs')
router.register('lyrics', LyricViewSet, basename='lyrics')

urlpatterns = router.urls
