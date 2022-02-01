from rest_framework.fields import CharField
from product.submodels.product import ProductModel
from rest_framework.serializers import ModelSerializer


class ListProductSerializer(ModelSerializer):
    category = CharField(source='category.title')

    class Meta:
        model = ProductModel
        fields = ('title', 'category',)
