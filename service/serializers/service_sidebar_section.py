from home_two.submodels.preview_item import PhotoModel
from service.models import ServiceSidebarSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveServiceSidebarSectionModelSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)
    section_image  = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = ServiceSidebarSectionModel
        fields = ('heading', 'summary', 'section_image',
                  'background_image',)
