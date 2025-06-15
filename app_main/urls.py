from django.urls import path
from .views import GameLevelListAPIView

urlpatterns = [
    path('api/levels/', GameLevelListAPIView.as_view(), name='game-levels-list'),
]
