from product.submodels.rating_scale import  ProductReviewModel
from rest_framework.serializers import ModelSerializer


class ListProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReviewModel
        fields = ('rating', 'review',)


class AddProductReviewSerializer(ModelSerializer):
    pass
