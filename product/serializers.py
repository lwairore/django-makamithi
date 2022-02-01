from product.submodels.category import ProductCategoryModel
from rest_framework.serializers import ModelSerializer


class ListProductCategorySerializer(ModelSerializer):
    class Model:
        model = ProductCategoryModel
        fields = ('title', 'description',)
