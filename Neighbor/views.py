from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *


class NeighborhoodList(APIView):
    def get(self, request, format=None):
        all_hood = Neighborhood.objects.all()
        serializers = NeighborhoodSerializer(all_hood, many=True)
        return Response(serializers.data)