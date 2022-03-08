from home_two.submodels.preview_item import PhotoModel
from partner.models import PartnerModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrievePartnerModelSerializer(ModelSerializer):
    image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = PartnerModel
        fields = ('title', 'link', 'image')
