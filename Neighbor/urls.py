from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

urlpatterns = [
    path('api/post/auth/signup', views.MerchList.as_view()),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/neighborhood/', views.NeighborhoodList.as_view()),
    path('api/neighborhood/neighborhood-id/<int:pk>/', views.NeighborhoodDescription.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/profile/profile-id/<int:pk>/', views.ProfileDescription.as_view()),
    
]
