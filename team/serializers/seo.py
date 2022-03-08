from team.models import TeamSEODetailsModel
from social_sharing.serializers.image_aux_data import ImageAuxDataModelSerializer
from rest_framework.serializers import ModelSerializer


class RetrieveTeamSEODetailsModelSerializer(ModelSerializer):
    image = ImageAuxDataModelSerializer(required=False)

    class Meta:
        model = TeamSEODetailsModel
        fields = ('title', 'keywords', 'description', 'image',
                  'type', 'author', 'section', 'published', 'modified')
