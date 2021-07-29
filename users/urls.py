from django.urls import include, path
from rest_framework import routers
from .views import UserView

router = routers.SimpleRouter()
router.register(r'', UserView, basename='Users')

urlpatterns = [
    path('users/', include(router.urls)),
]
