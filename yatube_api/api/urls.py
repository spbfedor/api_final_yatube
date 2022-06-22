from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet, CustomUserViewSet, FollowViewSet,
                       GroupViewSet, PostViewSet)

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='followers')
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
