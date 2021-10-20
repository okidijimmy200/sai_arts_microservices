from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from pictures.models import ArtPiece
from pictures import serializers


class ArtPieceViewSet(viewsets.ModelViewSet):
    '''manage artpiece in the db'''
    serializer_class = serializers.ArtPieceSerializer
    queryset = ArtPiece.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

        # return artpiece for user
    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(user=self.request.user)

    # @action(detail=True, methods=['post'])
    def perform_create(self, serializer):
        '''create a new artpiece'''
        serializer.save(user=self.request.user)






