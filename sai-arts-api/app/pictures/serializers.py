from django.db import models
from rest_framework import serializers
from .models import ArtPiece

class ArtPieceSerializer(serializers.ModelSerializer):
    '''serialize a picture'''
    class Meta:
        model = ArtPiece
        fields = ('id', 'name', 'publish_date', 'slug', 'body', 'status')
        read_only_fields = ('id',)
