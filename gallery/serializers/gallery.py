from home_two.submodels.preview_item import PhotoModel
from gallery.models import GalleryModel
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveGalleryModelForGalleryPageSerializer(ModelSerializer):
    category = CharField(source='category.title', required=False)
    gallery_preview = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = GalleryModel
        fields = ('id', 'gallery_preview', 'category', 'title',)


class RetrieveGalleryDetailModelSerializer(ModelSerializer):
    category = CharField(source='category.title', required=False)
    layout_image = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = GalleryModel
        fields = ('layout_image', 'category', 'title', 'keywords', 'description',
        'occured_on',)
