from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from .models import Moon
from .serializers import MoonSerializer


class MoonList(generics.ListCreateAPIView):
    queryset = Moon.objects.all()
    serializer_class = MoonSerializer


class MoonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moon.objects.all()
    serializer_class = MoonSerializer
