from home_two.submodels.preview_item import PhotoModel
from rest_framework.serializers import ModelSerializer


class ImageAuxDataModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('width', 'height', 'image', 'caption',)
