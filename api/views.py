from rest_framework import viewsets, permissions, status
from django.contrib.auth import get_user_model
from api.serializers import *
from rest_framework.response import Response

UserModel = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    default_serializer_class = UserOutputSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserInputSerializer
        return UserOutputSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserModel.objects.create_user(**serializer.validated_data)
        return Response(UserOutputSerializer(user).data, status=status.HTTP_201_CREATED)

class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
