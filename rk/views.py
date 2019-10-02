from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DeedSerializer
from .models import Deed

class DeedView(viewsets.ModelViewSet):
    serializer_class = DeedSerializer
    queryset = Deed.objects.all()
