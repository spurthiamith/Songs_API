from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Audiobook, Podcast, Song
from .serializer import AudiobookSerializer, PodcastSerializer, SongSerializer


class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            res = {'msg': 'Delete process successfull'}
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PodcastModelViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            res = {'msg': 'Delete process successfull'}
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class AudiobookModelViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            res = {'msg': 'Delete process successfull'}
            return Response(res, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
def create_api(request):
    try:
        if request.method == "POST":
            if (request.data["file_type"] == "song"):
                serializer = SongSerializer(data=request.data["meta_data"])
                if serializer.is_valid():
                    serializer.save()
                    res = {'msg': 'Song Data Created'}
                    return Response(res, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if (request.data["file_type"] == "podcast"):
                serializer = PodcastSerializer(data=request.data["meta_data"])
                if serializer.is_valid():
                    serializer.save()
                    res = {'msg': 'Podacast Data Created'}
                    return Response(res, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if (request.data["file_type"] == "audiobook"):
                serializer = AudiobookSerializer(data=request.data["meta_data"])
                if serializer.is_valid():
                    serializer.save()
                    res = {'msg': 'Audiobook Data Created'}
                    return Response(res, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
