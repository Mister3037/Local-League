from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('team-list/', TeamAPIView.as_view(), name='team-list'),
    path('contact/', ContactAPIView.as_view(), name='contact'),
    path('team-list/<int:pk>/', TeamDetailAPIView.as_view(), name='team-detail'),
    path('profile/<int:pk>/', ProfileAPIView.as_view(), name='profile'),
    path('news/', NewsAPIView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('player/<int:pk>/', PlayerAPIView.as_view(), name='player'),
]