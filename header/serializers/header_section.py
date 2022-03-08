from home_two.submodels.preview_item import PhotoModel
from header.models import HeaderSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveHeaderSectionForTopHeaderModelSerializer(ModelSerializer):
    class Meta:
        model = HeaderSectionModel
        fields = ('primary_location', 'whatsapp_business_number',)

class RetrieveLogosForStickyHeaderSectionSerializer(ModelSerializer):
    retina_logo = _RetrievePhotoModelSerializer(required=False)
    standard_logo = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = HeaderSectionModel
        fields = ('standard_logo', 'retina_logo',)