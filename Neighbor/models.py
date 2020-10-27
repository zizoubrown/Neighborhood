from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    details = models.CharField(max_length=150, null=True, blank=True)
    contact_info = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
		return self.name

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
		return self.user.username

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

