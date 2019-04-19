from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404
from django.db.models import Q

from products.models import Product

class SearchListView(ListView):
	template_name = "search/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		query = request.GET.get('q', None) # None is the default here. We can put in for example 'shirt' as default.
		if query is not None:
			lookups = (	Q(title__icontains=query) | 
						Q(description__icontains=query) |
						Q(price__icontains=query) |
						Q(tag__title__icontains=query) )
			return Product.objects.filter(lookups).distinct()
		return None
