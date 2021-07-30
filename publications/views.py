from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Publication, Like
from .serializers import PublicationSerializer
from .utils import update_last_request


class PublicationView(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        update_last_request(self.request.user)
        return Publication.objects.all()

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated])
    def create_publication(self, request, *args, **kwargs):
        title = request.data.get('title')
        body = request.data.get('body')
        user = request.user
        if title is None:
            return Response('Input title', status=status.HTTP_400_BAD_REQUEST)
        if len(title) <= 8:
            return Response('Title must be longer than 8 characters', status=status.HTTP_400_BAD_REQUEST)
        publication = Publication.objects.create(
            title=title,
            body=body,
            user=user
        )
        publication.save()
        update_last_request(self.request.user)
        serializer = self.serializer_class(publication)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['PUT'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, *args, **kwargs):
        user = request.user
        publication = self.get_object()
        if publication.likes.filter(user=user):
            publication.likes.filter(user=user)[0].delete()
            publication.save()
            response = {
                'number_of_likes': len(publication.likes.values()),
                'likes': publication.likes.values()
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        like = Like.objects.create(
            user=user
        )
        like.save()
        publication.likes.add(like)
        publication.save()
        update_last_request(self.request.user)
        response = {
            'number_of_likes': len(publication.likes.values()),
            'likes': publication.likes.values()
        }
        return Response(response, status=status.HTTP_200_OK)
