from rest_framework import serializers

from products.models import Product

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'image',
        ]

    def validate_description(self, value):
        if len(value) > 10000:
            raise serializers.ValidationError("Description way too long!!!")
        return value

class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
        read_only_fields = ['title']

