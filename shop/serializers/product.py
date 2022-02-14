from home_two.submodels.preview_item import PhotoModel
from rest_framework.fields import DecimalField
from shop.submodels.product import ProductModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveProductSerializer(ModelSerializer):
    photo = _RetrievePhotoModelSerializer(required=False)
    price = DecimalField(source='price.now', required=False, max_digits=10,
                         decimal_places=2)

    class Meta:
        model = ProductModel
        fields = ('title', 'price', 'id', 'photo',)
