from home_two.submodels.preview_item import PhotoModel
from service.submodels.service import ServiceModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveServiceModelSerializer(ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ('photo', 'id', 'title', 'summary')
