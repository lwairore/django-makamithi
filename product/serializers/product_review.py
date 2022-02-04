from django.db.models.query import QuerySet
from rest_framework.exceptions import ValidationError
from product.submodels.product import ProductModel
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


class _AddProductReviewSerializer(ModelSerializer):

    class Meta:
        model = ProductReviewModel
        fields = ('rating', 'review',)

    def create(self, validated_data):
        new_review = ProductReviewModel.objects.create(**validated_data)

        return new_review


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

    def manually_handle_put_for_non_existing_models(self, product_instance: ProductModel,  updated_details):
        detail_to_note = {}

        new_review_serializer = _AddProductReviewSerializer(
            data=updated_details)

        if not new_review_serializer.is_valid():
            raise ValidationError(detail=new_review_serializer.errors)

        new_review: ProductReviewModel = new_review_serializer.save()

        product_instance.reviews.add(new_review)

        detail_to_note['id'] = new_review.id

        return detail_to_note

    def manually_handle_put_for_existing_models(self, product_instance: ProductModel, updated_details):
        if not check_key(updated_details, 'id'):
            try:
                return self.manually_handle_put_for_non_existing_models(
                    product_instance, updated_details)
            except ValidationError as validation_error:
                raise validation_error

        review_id = updated_details.get('id')

        review_kueryset: QuerySet = product_instance.reviews\
            .filter(id=review_id)

        if not review_kueryset.exists():
            raise ValidationError({
                'reviews':
                    [f'Object with id={review_id} does not exist.']
            })

        review_instance: ProductReviewModel = review_kueryset.first()

        if check_key(updated_details, 'rating'):
            updated_rating = updated_details.get('rating')

            if updated_rating != review_instance.rating:
                review_instance.rating = updated_rating
                review_instance.save(update_fields=['rating', ])

        if check_key(updated_details, 'review'):
            updated_review = updated_details.get('review')

            if updated_review != review_instance.review:
                review_instance.review = updated_review
                review_instance.save(update_fields=['review', ])

        return review_instance

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


class UpdateProductReviewGatewaySerializer(ModelSerializer):
    reviews = UpdateProductReviewSerializer()

    class Meta:
        model = ProductModel
        fields = ('reviews',)

    def update(self, instance: ProductModel, validated_data):
        updated_details = validated_data.pop('reviews')

        if instance.reviews.all().exists():
            return UpdateProductReviewSerializer()\
                .manually_handle_put_for_existing_models(instance, updated_details)
        else:
            return UpdateProductReviewSerializer()\
                .manually_handle_put_for_non_existing_models(instance, updated_details)
