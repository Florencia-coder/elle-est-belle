from .models import Comments, Album
from rest_framework import viewsets, permissions
from .serelizers import CommentSerializer, AlbumSerealizer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlbumSerealizer
