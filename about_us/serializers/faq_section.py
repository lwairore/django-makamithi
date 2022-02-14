from about_us.submodels.faq_section import FaqSectionModel
from home_two.models import PhotoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveFaqSectionModelSerializer(ModelSerializer):
    class Meta:
        model = FaqSectionModel
        fields = ('title', 'background_image',)
