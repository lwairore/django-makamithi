from shop.submodels.product_review import ProductReview
from shop.submodels.price import PriceModel
from home_two.submodels.preview_item import PhotoModel
from rest_framework.fields import DecimalField, IntegerField
from shop.submodels.product import ProductModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveProductSerializer(ModelSerializer):
    product_preview = _RetrievePhotoModelSerializer(required=False)
    price = DecimalField(source='price.now', required=False, max_digits=10,
                         decimal_places=2)

    class Meta:
        model = ProductModel
        fields = ('title', 'price', 'id', 'product_preview',
                  'total_sales',)


class _RetrievePriceModelSerializer(ModelSerializer):
    class Meta:
        model = PriceModel
        fields = ('was', 'now',)


class RetrieveProductDetailSerializer(ModelSerializer):
    total_reviews = IntegerField(default=0)
    price = _RetrievePriceModelSerializer(required=False)
    product_images = _RetrievePhotoModelSerializer(many=True, required=False)

    class Meta:
        model = ProductModel
        fields = ('title', 'price', 'keywords', 'product_images', 'description',
                  'total_sales', 'created_at', 'modified_date', 'total_reviews',)
