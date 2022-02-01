from product.submodels.price import PriceModel
from rest_framework.fields import CharField
from product.submodels.product import ProductModel
from rest_framework.serializers import ModelSerializer


class _ListPriceModelSerializer(ModelSerializer):
    class Meta:
        model = PriceModel
        fields = ('was', 'now', 'per',)


class ListProductSerializer(ModelSerializer):
    category = CharField(source='category.title')

    class Meta:
        model = ProductModel
        fields = ('title', 'category',)
