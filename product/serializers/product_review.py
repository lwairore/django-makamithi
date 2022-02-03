from product.submodels.rating_scale import FivePointRatingScaleModel
from rest_framework.serializers import ModelSerializer


class ListProductReviewSerializer(ModelSerializer):
    class Meta:
        model = FivePointRatingScaleModel
        fields = ('five_star', 'four_star',
                  'three_star', 'two_star', 'one_star',)
