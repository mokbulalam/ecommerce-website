import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator

def get_filename_ext(filename):
	base_name = os.path.basename(filename)
	name, ext = os.path.splitext(filename)
	return name, ext

def upload_image_path(instance, filename):
	new_filename = random.randint(1,97322874623746374874)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/product_images/{final_filename}".format(final_filename=final_filename)

class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def search(self, query):
		lookups = Q(title__icontains=query) | Q(description__icontains=query)
		return self.filter(lookups).distinct()

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def search(self, query):
		return self.get_queryset().search(query)

class Product(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField()
	price 		= models.DecimalField(decimal_places=2, max_digits=20, default=59.99)
	image 		= models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	def get_absolute_url(self):
		return reverse("products:product_detail", kwargs={'pk':self.pk})

	def __str__(self):
		return self.title

# def product_pre_save_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)

# pre_save.connect(product_pre_save_receiver, sender=Product)