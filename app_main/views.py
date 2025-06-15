from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GameLevel
from .serializers import GameLevelSerializer

class GameLevelListAPIView(APIView):
    def get(self, request):
        levels = GameLevel.objects.all().order_by('id')
        serializer = GameLevelSerializer(levels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
