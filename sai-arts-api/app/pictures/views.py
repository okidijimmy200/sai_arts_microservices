from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from pictures.models import ArtPiece
from pictures import serializers

# class BaseArtPieceViewSet(viewsets.GenericViewSet,
#                           mixins.ListModelMixin,
#                           mixins.CreateModelMixin):
#     # base viewset for user owned artpiece attr
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self):
#         '''return objects for authenticated user only'''
#         assigned_only = bool(self.request.query_params.get('assigned_only'))
#         queryset = self.queryset
#         if assigned_only:
#             queryset = queryset.filter(artpiece__isnull=False)
#         return queryset.filter(user=self.request.user).order_by('-name')

#     def perform_create(self, serializer):
#         '''create a new object'''
#         serializer.save(user=self.request.user)

class ArtPieceViewSet(viewsets.ModelViewSet):
    '''manage artpiece in the db'''
    serializer_class = serializers.ArtPieceSerializer
    queryset = ArtPiece.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['post'])
    def perform_create(self, serializer):
        '''create a new artpiece'''
        serializer.save(user=self.request.user)

    # return artpiece for user
    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(user=self.request.user)




