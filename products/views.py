from django.views.generic import ListView, DetailView
from django.shortcuts import render,get_object_or_404

from .models import Product
from carts.models import Cart

class ProductListView(ListView):
	# queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		cart_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context

class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		cart_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context

# class ProductDetailSlugView(DetailView):
# 	queryset = Product.objects.all()
# 	template_name = "products/detail.html"

# 	def get_object(self, *args, **kwargs):
# 		request = self.request
# 		slug = self.kwargs.get('slug')
# 		instance = get_object_or_404(Product, slug=slug)
# 		return instance