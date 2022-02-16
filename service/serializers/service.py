from home_two.submodels.preview_item import PhotoModel
from service.submodels.service import ServiceModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveServiceModelSerializer(ModelSerializer):
    home_photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = ServiceModel
        fields = ('home_photo', 'id', 'title', 'summary')
