from home_two.submodels.preview_item import PhotoModel
from service.submodels.service import ServiceModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveHomeServiceModelSerializer(ModelSerializer):
    home_photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = ServiceModel
        fields = ('home_photo', 'id', 'title', 'summary')


class RetrieveAboutServiceModelSerializer(ModelSerializer):
    about_photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = ServiceModel
        fields = ('about_photo', 'id', 'title', 'summary')
