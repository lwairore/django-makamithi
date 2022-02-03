from custom_utils.dict_is_not_empty import dict_is_not_empty
from custom_utils.string_is_not_empty import string_is_not_empty
from custom_utils.check_key_util import check_key
from django.db.models import fields
from rest_framework.fields import IntegerField
from product.submodels.rating_scale import ProductReviewModel
from rest_framework.serializers import ModelSerializer


class ListProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReviewModel
        fields = ('rating', 'review',)


class UpdateProductReviewSerializer(ModelSerializer):
    id = IntegerField(required=False)

    def format_request_data(self, request_data):
        formatted_review = {}

        if check_key(request_data, 'rating'):
            value_for_rating = request_data.get('rating')

            if string_is_not_empty(value_for_rating):
                formatted_review['rating'] = value_for_rating

        if check_key(request_data, 'review'):
            value_for_review = request_data.get('review')

            if string_is_not_empty(value_for_review):
                formatted_review['review'] = value_for_review

        return formatted_review if dict_is_not_empty(formatted_review) else None

    class Meta:
        model = ProductReviewModel
        fields = ('rating', 'review', 'id',)
        extra_kwargs = {
            'rating': {
                'required': False
            },
            'review': {
                'required': False
            },
        }
