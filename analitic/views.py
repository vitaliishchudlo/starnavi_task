import datetime

from publications.models import Like
from rest_framework import generics, status
from rest_framework.response import Response
from users.models import User


class AnaliticsView(generics.GenericAPIView):
    # serializer_class = serializers.UidAndTokenSerializer
    permission_classes = []

    def get(self, request):
        try:
            date_from = datetime.datetime.strptime(request.query_params.get('date_from'), '%Y-%m-%d')
            date_to = datetime.datetime.strptime(request.query_params.get('date_to'), '%Y-%m-%d')
            date_to += datetime.timedelta(days=1)
        except Exception:
            return Response('Correctly fill in parameters: date_from and date_to', status=status.HTTP_400_BAD_REQUEST)
        likes = Like.objects.filter(created__gte=date_from, created__lte=date_to)
        if likes.count() == 0:
            return Response('No likes during this period.', status=status.HTTP_204_NO_CONTENT)
        ordered_likes = likes.values().order_by('created')  # from older to newer
        response = {}
        for day in ordered_likes:
            date = day['created']
            result = f'{date:%y}-{date:%m}-{date:%d}'
            if response.get(result):
                response[result] = response.get(result) + 1
            else:
                response[result] = 1
        return Response(response, status=status.HTTP_200_OK)


class UserView(generics.GenericAPIView):
    # serializer_class = serializers.UidAndTokenSerializer
    permission_classes = []

    def get(self, request):
        users = User.objects.all()
        last_requests = {}
        for user in users.values():
            last_requests[user['username']] = datetime.datetime.strftime(user['last_request'], '%Y-%m-%d %H:%M:%S')
        return Response([{'Last requests': last_requests}, {'Last logins': ''}], status=status.HTTP_200_OK)
