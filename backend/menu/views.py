from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import MenuItem
from .serializers import MenuItemSerializer

# List all menu items (optionally filter by category field in MenuItem if it exists)
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def menu_items(request):
    category = request.GET.get('category')
    items = MenuItem.objects.filter(archived=False)
    if category and hasattr(MenuItem, 'category'):
        items = items.filter(category=category)
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)

# Get details of a single menu item
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def menu_item_detail(request, item_id):
    try:
        item = MenuItem.objects.get(id=item_id, archived=False)
    except MenuItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    serializer = MenuItemSerializer(item)
    return Response(serializer.data)

# Get availability of a menu item
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def menu_item_availability(request, item_id):
    try:
        item = MenuItem.objects.get(id=item_id, archived=False)
    except MenuItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    return Response({'id': str(item.id), 'name': item.name, 'available': item.available})

# Get image URL of a menu item
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def menu_item_image(request, item_id):
    try:
        item = MenuItem.objects.get(id=item_id, archived=False)
    except MenuItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    if not item.image:
        return Response({'error': 'No image found'}, status=404)
    return Response({'image_url': item.image.url})
