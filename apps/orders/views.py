from rest_framework.views import APIView
from rest_framework.response import Response

class CartView(APIView):
    def get(self, request):
        return Response({'detail': 'not implemented'})

class CartItemAddView(APIView):
    def post(self, request):
        return Response({'detail': 'not implemented'})

class CartItemUpdateView(APIView):
    def patch(self, request, pk):
        return Response({'detail': 'not implemented'})
    def delete(self, request, pk):
        return Response({'detail': 'not implemented'})

class OrderListCreateView(APIView):
    def get(self, request):
        return Response({'detail': 'not implemented'})
    def post(self, request):
        return Response({'detail': 'not implemented'})

class OrderDetailView(APIView):
    def get(self, request, pk):
        return Response({'detail': 'not implemented'})

class SellerOrderListView(APIView):
    def get(self, request):
        return Response({'detail': 'not implemented'})

class SellerOrderStatusView(APIView):
    def patch(self, request, pk):
        return Response({'detail': 'not implemented'})