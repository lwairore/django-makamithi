from social_sharing.serializers.image_aux_data import ImageAuxDataModelSerializer
from home_two.models import HomeSEODetailsModel
from rest_framework.serializers import ModelSerializer


class RetrieveHomeSEODetailsSerializer(ModelSerializer):
    image = ImageAuxDataModelSerializer(required=False)

    class Meta:
        model = HomeSEODetailsModel
        fields = ('title', 'keywords', 'description', 'image',
                  'type', 'author', 'section', 'published', 'modified')
