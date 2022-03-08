from home_two.models import CounterAreaSectionModel, PhotoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveCounterAreaSectionSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = CounterAreaSectionModel
        fields = ('heading', 'background_image',)
