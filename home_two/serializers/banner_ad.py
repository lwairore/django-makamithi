from home_two.models import PhotoModel
from home_two.submodels.banner_ad import BannerAdModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class ListBannerAdModelSerializer(ModelSerializer):
    photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = BannerAdModel
        fields = ('title', 'description', 'photo',)
