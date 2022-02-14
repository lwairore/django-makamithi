from home_two.submodels.preview_item import PhotoModel
from home_two.submodels.visit_now_cta_section import VisitNowCtaSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveVisitNowCtaSectionSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = VisitNowCtaSectionModel
        fields = ('heading', 'description',
                  'background_image', 'section_image',)
