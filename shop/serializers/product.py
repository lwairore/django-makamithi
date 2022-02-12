from rest_framework.fields import DecimalField
from shop.submodels.product import ProductModel
from rest_framework.serializers import ModelSerializer


class RetrieveProductSerializer(ModelSerializer):
    price = DecimalField(source='price.now', required=False, max_digits=10,
                         decimal_places=2)

    class Meta:
        model = ProductModel
        fields = ('title', 'price', 'id', 'photo',)
