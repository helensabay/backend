from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import MyTokenObtainPairSerializer
from .views import RegisterView
from .views import MyTokenObtainPairView, ProfileView  # <-- Import from views, NOT serializers

from .views import MyTokenObtainPairView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
