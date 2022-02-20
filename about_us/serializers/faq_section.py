from about_us.submodels.faq_section import FaqSectionModel
from home_two.submodels.preview_item import PhotoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveFaqSectionModelSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = FaqSectionModel
        fields = ('heading', 'background_image',)
