from home_two.submodels.preview_item import PhotoModel
from home_two.submodels import GallerySectionModel
from rest_framework.serializers import ModelSerializer

class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveGallerySectionModelSerializer(ModelSerializer):
    class Meta:
        model = GallerySectionModel
        fields = ('heading', 'summary', 'section_image',)
