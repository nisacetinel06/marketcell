from rest_framework import serializers
from .models import Cart, CartItem, Order, SubOrder, OrderItem, Coupon
from apps.products.serializers import ProductVariantSerializer


class CartItemSerializer(serializers.ModelSerializer):
    variant        = ProductVariantSerializer(read_only=True)
    variant_id     = serializers.UUIDField(write_only=True)
    product_name   = serializers.CharField(source='variant.product.name', read_only=True)
    unit_price     = serializers.SerializerMethodField()
    total_price    = serializers.SerializerMethodField()

    class Meta:
        model  = CartItem
        fields = ('id', 'variant', 'variant_id', 'quantity',
                  'product_name', 'unit_price', 'total_price')
        read_only_fields = ('id',)

    def get_unit_price(self, obj):
        return float(obj.variant.product.base_price + obj.variant.price_diff)

    def get_total_price(self, obj):
        unit = obj.variant.product.base_price + obj.variant.price_diff
        return float(unit * obj.quantity)


class CartSerializer(serializers.ModelSerializer):
    items       = CartItemSerializer(many=True, read_only=True)
    total       = serializers.SerializerMethodField()
    item_count  = serializers.SerializerMethodField()

    class Meta:
        model  = Cart
        fields = ('id', 'items', 'total', 'item_count', 'updated_at')

    def get_total(self, obj):
        total = 0
        for item in obj.items.all():
            total += (item.variant.product.base_price + item.variant.price_diff) * item.quantity
        return float(total)

    def get_item_count(self, obj):
        return obj.items.count()


class OrderItemSerializer(serializers.ModelSerializer):
    product_name   = serializers.CharField(source='variant.product.name', read_only=True)
    variant_detail = serializers.CharField(source='variant.value', read_only=True)

    class Meta:
        model  = OrderItem
        fields = ('id', 'product_name', 'variant_detail', 'quantity', 'unit_price')


class SubOrderSerializer(serializers.ModelSerializer):
    items      = OrderItemSerializer(many=True, read_only=True)
    store_name = serializers.CharField(source='store.name', read_only=True)

    class Meta:
        model  = SubOrder
        fields = ('id', 'store_name', 'subtotal', 'status',
                  'tracking_no', 'items', 'updated_at')
        read_only_fields = ('id', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    sub_orders = SubOrderSerializer(many=True, read_only=True)

    class Meta:
        model  = Order
        fields = ('id', 'total_amount', 'payment_status', 'card_last4',
                  'discount_amount', 'sub_orders', 'created_at')
        read_only_fields = ('id', 'created_at')


class CreateOrderSerializer(serializers.Serializer):
    address_id  = serializers.UUIDField()
    card_number = serializers.CharField(max_length=16)
    coupon_code = serializers.CharField(required=False, allow_blank=True)


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Coupon
        fields = ('id', 'code', 'discount_type', 'discount_value',
                  'min_order_amount', 'expires_at')