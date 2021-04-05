from rest_framework import serializers

from .models import Audiobook, Podcast, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'uploaded_time']


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = ['id', 'title', 'author',
                  'narrator', 'duration', 'uploaded_time']


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['id', 'name', 'duration',
                  'uploaded_time', 'host', 'participants']
