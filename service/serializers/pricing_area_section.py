from home_two.submodels.preview_item import PhotoModel
from service.models import PricingAreaSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrievePricingAreaSectionModelSerializer(ModelSerializer):
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = PricingAreaSectionModel
        fields = ('heading', 'summary',
                  'section_image',)
