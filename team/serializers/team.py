from home_two.submodels.preview_item import PhotoModel
from team.models import TeamModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveTeamModelSerializer(ModelSerializer):
    image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = TeamModel
        fields = ('full_name', 'role', 'image',
                  'facebook', 'twitter',)
