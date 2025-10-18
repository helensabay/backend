from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            # Use a custom backend if needed
            user = authenticate(username=email, password=password)
            if user:
                return Response({"success": True, "message": "Login successful"})
            return Response({"success": False, "message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
