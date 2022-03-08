from home_two.submodels.preview_item import PhotoModel
from partner.models import PartnerAreaSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrievePartnerAreaSectionModelSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = PartnerAreaSectionModel
        fields = (
            'background_image',)
