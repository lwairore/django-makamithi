from home_two.models import PhotoModel
from rest_framework.serializers import ModelSerializer


class ImageAuxDataModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('width', 'height', 'image', 'caption',)
