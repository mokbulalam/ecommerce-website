from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from products.models import Product
from .serializers import CreateProductSerializer, UpdateProductSerializer

class ProductListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes  = [SessionAuthentication]
    serializer_class 		= CreateProductSerializer

    def get_queryset(self):
    	qs = Product.objects.all()
    	query = self.request.GET.get('q')
    	if query is not None:
    		qs = qs.filter(description__icontains=query)
    	return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes  = [SessionAuthentication]
    queryset                = Product.objects.all()
    serializer_class        = UpdateProductSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class ProductCreateAPIView(generics.CreateAPIView):
#     permission_classes      = []
#     authentication_classes  = []
#     queryset              = Product.objects.all()
#     serializer_class      = ProductSerializer


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     permission_classes      = []
#     authentication_classes  = []
#     queryset                = Product.objects.all()
#     serializer_class        = ProductSerializer

# class ProductDeleteAPIView(generics.DestroyAPIView):
#     permission_classes      = []
#     authentication_classes  = []
#     queryset                = Product.objects.all()
#     serializer_class        = ProductSerializer
