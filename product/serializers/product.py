from product.submodels.product import ProductModel
from rest_framework.serializers import ModelSerializer


class ListProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('title', 'category',)
