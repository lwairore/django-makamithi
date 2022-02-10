from product.submodels.preview_item import PhotoModel
from product.submodels.banner_ad import BannerAdModel
from rest_framework.serializers import ModelSerializer


class _ListPhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class BannerAdModelSerializer(ModelSerializer):
    photos = _ListPhotoModelModelSerializer(many=True, required=False)

    class Meta:
        model = BannerAdModel
        fields = ('title', 'description', 'photos',)
