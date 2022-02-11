from shop.submodels.product_category import ProductCategory
from rest_framework.serializers import ModelSerializer


class RetrieveProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('title', 'flaticon', 'description', 'id',)
