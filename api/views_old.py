from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from .serializers import ProductSerializer

# class ProductListAPIView(APIView):
#     permission_classes      = []
#     authentication_classes  = []

#     def get(self, request, format=None):
#         qs = Product.objects.all()
#         serializer = ProductSerializer(qs, many=True)
#         return Response(serializer.data)


class ProductListAPIView(generics.ListAPIView):
    permission_classes      = []
    authentication_classes  = []
    serializer_class 		= ProductSerializer

    def get_queryset(self):
    	qs = Product.objects.all()
    	query = self.request.GET.get('q')
    	if query is not None:
    		qs = qs.filter(description__icontains=query)
    	return qs

class ProductCreateAPIView(generics.CreateAPIView):
    permission_classes      = []
    authentication_classes  = []
    queryset 				= Product.objects.all()
    serializer_class 		= ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    permission_classes      = []
    authentication_classes  = []
    queryset                = Product.objects.all()
    serializer_class        = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    permission_classes      = []
    authentication_classes  = []
    queryset                = Product.objects.all()
    serializer_class        = ProductSerializer

class ProductDeleteAPIView(generics.DestroyAPIView):
    permission_classes      = []
    authentication_classes  = []
    queryset                = Product.objects.all()
    serializer_class        = ProductSerializer
