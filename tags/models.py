from django.db import models

from products.models import Product

class Tag(models.Model):
	title = models.CharField(max_length=120)
	products = models.ManyToManyField(Product, blank=True)

	def __str__(self):
		return self.title