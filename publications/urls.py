from django.urls import include, path
from rest_framework import routers
from .views import PublicationView

router = routers.SimpleRouter()
router.register(r'', PublicationView, basename='Users')

urlpatterns = [
    path('publications/', include(router.urls)),
]
