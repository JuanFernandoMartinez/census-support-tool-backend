from .models import CensusTemplate, Category, Question, CensusRecord, CensusResponse, Community
from .serializers import ComunitySerializer  # Import the ComunitySerializer class
from rest_framework import viewsets, permissions

class ComunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ComunitySerializer
    