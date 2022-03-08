from home_two.submodels.preview_item import PhotoModel
from gallery.models import GalleryDetailSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveGalleryDetailSectionModelSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = GalleryDetailSectionModel
        fields = ('background_image',)
