from home_two.submodels.preview_item import PhotoModel
from contact_us.models import WorkWithUsCtaSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveWorkWithUsCtaSectionSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = WorkWithUsCtaSectionModel
        fields = ('heading', 'description', 'call_to_action',
                  'background_image', 'section_image',)
