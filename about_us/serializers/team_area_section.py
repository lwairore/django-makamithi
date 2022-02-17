from home_two.submodels.preview_item import PhotoModel
from about_us.models import TeamAreaSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveTeamAreaSectionModelSerializer(ModelSerializer):
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = TeamAreaSectionModel
        fields = ('heading', 'summary',
                  'section_image',)
