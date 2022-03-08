from shop.submodels.product_review import ProductReview
from home_two.submodels.preview_item import PhotoModel
from rest_framework.serializers import ModelSerializer



class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)
        
class RetrieveProductReviewSerializer(ModelSerializer):
    client_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = ProductReview
        fields = ('full_name', 'client_image', 'review', 'created_at',
                  'rating',)
