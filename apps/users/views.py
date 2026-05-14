from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterView(APIView):
    def post(self, request):
        return Response({'detail': 'not implemented'})

class VerifyOTPView(APIView):
    def post(self, request):
        return Response({'detail': 'not implemented'})

class AddressListCreateView(APIView):
    def get(self, request):
        return Response({'detail': 'not implemented'})
    def post(self, request):
        return Response({'detail': 'not implemented'})

class AddressDetailView(APIView):
    def get(self, request, pk):
        return Response({'detail': 'not implemented'})
    def patch(self, request, pk):
        return Response({'detail': 'not implemented'})
    def delete(self, request, pk):
        return Response({'detail': 'not implemented'})