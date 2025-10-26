# accounts/urls.py
from django.urls import path
from .views import MyTokenObtainPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # JWT login
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration (public)
    path('register/', RegisterView.as_view(), name='register'),
]
