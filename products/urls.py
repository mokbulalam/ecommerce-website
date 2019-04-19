from django.urls import path

from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('detail/<pk>/', ProductDetailView.as_view(), name='product_detail'),
]
