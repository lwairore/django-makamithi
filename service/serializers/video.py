from home_two.submodels.preview_item import PhotoModel
from service.models import VideoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveVideoModelSerializer(ModelSerializer):
    thumbnail = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = VideoModel
        fields = ('title', 'caption',
                  'thumbnail', 'video',)
