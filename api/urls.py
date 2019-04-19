from django.urls import path
from .views import (
	ProductListAPIView, 
	ProductDetailAPIView,
	# ProductCreateAPIView,
	# ProductUpdateAPIView,
	# ProductDeleteAPIView,
	)

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    # path('create/', ProductCreateAPIView.as_view()),
    path('detail/<pk>/', ProductDetailAPIView.as_view()),
    # path('update/<pk>/', ProductUpdateAPIView.as_view()),
    # path('delete/<pk>/', ProductDeleteAPIView.as_view()),
]

