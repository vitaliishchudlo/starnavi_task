import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .utils import update_last_request


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        update_last_request(self.request.user)
        return User.objects.all()

    @action(methods=['POST'], detail=False, permission_classes=[])
    def register(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        re_password = request.data.get('re_password')
        if not username or not password or not re_password:
            return Response(
                [{'username': 'This field is required.',
                  'password': 'This field is required.',
                  're_password': 'This field is required.'}],
                status=status.HTTP_403_FORBIDDEN)
        if password != re_password:
            return Response("Passwords do not match.", status=status.HTTP_403_FORBIDDEN)
        user = User.objects.create(
            username=username,
            last_login=datetime.datetime.now(),
            last_request=datetime.datetime.now()
        )
        user.set_password(password)
        user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
