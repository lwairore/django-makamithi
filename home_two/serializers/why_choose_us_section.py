from home_two.submodels.preview_item import PhotoModel
from home_two.submodels import WhyChooseUsSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveWhyChooseUsSectionSerializer(ModelSerializer):
    class Meta:
        model = WhyChooseUsSectionModel
        fields = ('heading', 'description', 'section_image',)
