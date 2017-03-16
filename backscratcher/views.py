from rest_framework import viewsets

from .models import Backscratcher
from .serializers import BackscratcherSerializer


class BackscratcherViewSet(viewsets.ModelViewSet):
    queryset = Backscratcher.objects\
        .order_by('price').all()
    serializer_class = BackscratcherSerializer
