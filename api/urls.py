from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    ProjectListAPIView, ServiceListAPIView, ContactCreateAPIView,
    DashboardStatsAPIView
)

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='projects'),
    path('services/', ServiceListAPIView.as_view(), name='services'),
    path('contact/', ContactCreateAPIView.as_view(), name='contact'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashboard/', DashboardStatsAPIView.as_view(), name='dashboard'),
]