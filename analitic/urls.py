from django.urls import path

from .views import AnaliticsView, UserView

urlpatterns = [
    path('analitic/likes/', AnaliticsView.as_view()),
    path('analitic/users/', UserView.as_view())
]
