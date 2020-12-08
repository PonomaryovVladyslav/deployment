from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from myapp.API.serializers import ItemGetSerializer, ItemCreateSerializer, OrderGetSerializer
from myapp.models import Item, Order


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ItemGetSerializer
        return ItemCreateSerializer


class OrderViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderGetSerializer
