from myapp.models import Item, Order
from rest_framework.serializers import ModelSerializer


class ItemCreateSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'description', 'amount_available')


class ItemGetSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderGetSerializer(ModelSerializer):
    item = ItemGetSerializer()

    class Meta:
        model = Order
        fields = '__all__'
#
# class OrderSerializer(ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ('user', 'item', 'create_date', 'amount')
#
#
# class ItemSerializer(ModelSerializer):
#     orders = OrderSerializer(many=True)
#
#     class Meta:
#         model = Item
#         fields = ('name', 'description', 'amount_available', 'price', 'orders')
