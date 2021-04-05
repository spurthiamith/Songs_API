from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AudiobookModelViewSet, PodcastModelViewSet,
                    SongModelViewSet, create_api)

# Creating Router Object
router_song = DefaultRouter()
router_podcast = DefaultRouter()
router_audiobook = DefaultRouter()


# Regestering Class ViewSet to router
router_song.register('song', SongModelViewSet, basename='song')
router_audiobook.register('audiobook', AudiobookModelViewSet, basename='audiobook')
router_podcast.register('podcast', PodcastModelViewSet, basename='podcast')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/', create_api),
    path('api/', include(router_song.urls)),
    path('api/', include(router_podcast.urls)),
    path('api/', include(router_audiobook.urls)),
]
