from rest_framework import serializers
from .models import *

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ('id','neighborhood_name', 'neighborhood_location', 'occupants_count')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user', 'name', 'location','neighborhood_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'email', 'status','neighborhood')

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id','business_name', 'user', 'business_email','neighborhood')

