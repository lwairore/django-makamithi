from shop.submodels.product_category import ProductCategoryModel
from rest_framework.serializers import ModelSerializer


class RetrieveProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = ('title', 'flaticon', 'description', 'id',)
