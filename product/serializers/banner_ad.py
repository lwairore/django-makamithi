from product.submodels.banner_ad import BannerAdModel
from rest_framework.serializers import ModelSerializer


class BannerAdModelSerializer(ModelSerializer):
    class Meta:
        model = BannerAdModel
        fields = ('title', 'description', 'photos',)
