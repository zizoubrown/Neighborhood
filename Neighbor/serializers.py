from rest_framework import serializers
from .models import *

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('neighborhood_name', 'neighborhood_location', 'occupants_count','admin')

