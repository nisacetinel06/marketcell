from rest_framework.views import APIView
from rest_framework.response import Response

class ProductListView(APIView):
    def get(self, request):
        return Response({'detail': 'not implemented'})

class ProductDetailView(APIView):
    def get(self, request, pk):
        return Response({'detail': 'not implemented'})

class CategoryListView(APIView):
    def get(self, request):
        return Response({'detail': 'not implemented'})

class StoreListCreateView(APIView):
    def get(self, request):
        return Response({'detail': 'not implemented'})
    def post(self, request):
        return Response({'detail': 'not implemented'})