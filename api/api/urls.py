from rest_framework import routers
from .api import CommentViewSet, AlbumViewSet

router = routers.DefaultRouter()

router.register('api/comments', CommentViewSet, "comments")
router.register('api/album', AlbumViewSet, 'album' )

urlpatterns = router.urls