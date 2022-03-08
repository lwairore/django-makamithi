from home_two.submodels.preview_item import PhotoModel
from footer.models import FooterSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveFooterSectionSerializer(ModelSerializer):
    footer_logo = _RetrievePhotoModelSerializer(required=False)
    background_image = _RetrievePhotoModelSerializer(required=False)
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = FooterSectionModel
        fields = ('footer_text', 'footer_logo', 'background_image',
                  'section_image',)
