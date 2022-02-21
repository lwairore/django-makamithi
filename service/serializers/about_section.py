from home_two.submodels.preview_item import PhotoModel
from service.models import ServiceAboutSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveServiceAboutSectionModelSerializer(ModelSerializer):
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = ServiceAboutSectionModel
        fields = ('heading', 'description',
                  'section_image',)
