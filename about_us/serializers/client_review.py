from home_two.submodels.preview_item import PhotoModel
from about_us.models import ClientReviewModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveClientReviewModelSerializer(ModelSerializer):
    image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = ClientReviewModel
        fields = ('full_name', 'review', 'image',)
