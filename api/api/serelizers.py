from rest_framework import serializers
from .models import Comments, Album

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'title', 'description', 'created_at')
        read_only_fields = ('created_at',)

class AlbumSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'month', 'images')