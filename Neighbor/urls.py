from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/post/auth/signup', views.MerchList.as_view()),
     path('api/neighborhood/', views.NeighborhoodList.as_view()),
]