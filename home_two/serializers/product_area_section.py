from home_two.models import ProductAreaSectionModel
from home_two.submodels.preview_item import PhotoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveProductAreaSectionSerializer(ModelSerializer):
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = ProductAreaSectionModel
        fields = ('summary', 'section_image', 'heading',)
