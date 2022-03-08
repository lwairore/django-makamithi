from contact_us.models import LeaveUsAMessageSectionModel
from home_two.submodels.preview_item import PhotoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveLeaveUsAMessageSectionModelSerializer(ModelSerializer):
    background_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = LeaveUsAMessageSectionModel
        fields = ('heading', 'background_image', 'summary', 'our_promise',)
