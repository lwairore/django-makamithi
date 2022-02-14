from home_two.models import PhotoModel
from home_two.submodels import GallerySectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveGallerySectionModelSerializer(ModelSerializer):
    section_image = _RetrievePhotoModelSerializer(required=False)
    background_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = GallerySectionModel
        fields = ('heading', 'summary', 'section_image',
                  'background_image',)
