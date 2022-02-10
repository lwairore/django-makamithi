from home_two.submodels.preview_item import PhotoModel
from home_two.submodels.banner_ad import BannerAdModel
from rest_framework.serializers import ModelSerializer


class _ListPhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class ListBannerAdModelSerializer(ModelSerializer):
    photos = _ListPhotoModelModelSerializer(many=True, required=False)

    class Meta:
        model = BannerAdModel
        fields = ('title', 'description', 'photos',)
