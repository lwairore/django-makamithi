from home_two.submodels.our_feature_section import FeatureSectionModel
from home_two.submodels.preview_item import PhotoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveFeatureSectionSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = FeatureSectionModel
        fields = ('summary', 'background_image', 'section_image',)
