from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import NeighborhoodSerializer, ProfileSerializer, UserSerializer, BusinessSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly



class NeighborhoodList(APIView):
    def get(self, request, format=None):
        all_neighborhood = Neighborhood.objects.all()
        serializers = NeighborhoodSerializer(all_neighborhood, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = NeighborhoodSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class NeighborhoodDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_neighborhood(self, pk):
        try:
            return Neighborhood.objects.get(pk=pk)
        except Neighborhood.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        neighborhood = self.get_neighborhood(pk)
        serializers = NeighborhoodSerializer(neighborhood)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        neighborhood = self.get_neighborhood(pk)
        serializers = NieghborhoodSerializer(neighborhood, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        neighborhood = self.get_neighborhood(pk)
        neighborhood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    def get(self, request, format=None):
        all_user = User.objects.all()
        serializers = UserSerializer(all_user, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        user = self.get_user(pk)
        serializers = UserSerializer(user)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        user = self.get_user(pk)
        serializers = UserSerializer(user, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BusinessList(APIView):
    def get(self, request, format=None):
        all_business = Business.objects.all()
        serializers = BusinessSerializer(all_business, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BusinessSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_business(self, pk):
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        business = self.get_business(pk)
        serializers = BusinessSerializer(business)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        business = self.get_business(pk)
        serializers = BusinessSerializer(business, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        business = self.get_business(pk)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)