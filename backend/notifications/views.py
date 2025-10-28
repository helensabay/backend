from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def list_notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user) | Notification.objects.filter(user=None)
    else:
        notifications = Notification.objects.filter(user=None)

    notifications = notifications.order_by('-created_at')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
