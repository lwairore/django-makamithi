from social_media.models import SocialMediaModel
from rest_framework.serializers import ModelSerializer


class RetrieveSocialMediaSerializer(ModelSerializer):

    class Meta:
        model = SocialMediaModel
        fields = ('link', 'title', 'icon',)
