from home_two.submodels.preview_item import PhotoModel
from gallery.submodels.gallery import GalleryModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class ListHomeGallerySerializer(ModelSerializer):
    image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = GalleryModel
        fields = ('image',)
