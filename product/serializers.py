from product.submodels.category import ProductCategoryModel
from rest_framework.serializers import ModelSerializer


class ListProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = ('title', 'description',)
