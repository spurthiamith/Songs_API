from django.contrib import admin
from .models import Song, Podcast, Audiobook


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration', 'uploaded_time']


@admin.register(Podcast)
class PodcasttAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration',
                    'uploaded_time', 'host', 'participants']


@admin.register(Audiobook)
class AudiobookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author',
                    'narrator', 'duration', 'uploaded_time']
