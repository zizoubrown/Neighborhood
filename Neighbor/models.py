from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=50, null=True, blank=True)
    neighborhood_location = models.CharField(max_length=50, null=True, blank=True)
    occupants_count = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.neighborhood_name
    

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    neighborhood_name = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighborhood')
    
    def __str__(self):
        return self.user
    
    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class User(models.Model):
    name =  models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create_user(self):
        self.save()

    def delete_user(self):
        self.delete()

class Business(models.Model):
    business_name = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business')
    business_email = models.EmailField(max_length=100, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save

    def delete_business(self):
        self.delete()
    
    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()