from home_two.submodels.preview_item import PhotoModel
from about_us.submodels.ap_about_section import ApAboutSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveApAboutSectionModelSerializer(ModelSerializer):
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = ApAboutSectionModel
        fields = ('heading', 'subheading', 'description',
                  'section_image',)
