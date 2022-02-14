from about_us.models import AboutUsSEODetailsModel
from social_sharing.serializers.image_aux_data import ImageAuxDataModelSerializer
from rest_framework.serializers import ModelSerializer


class RetrieveAboutUsSEODetailsModelSerializer(ModelSerializer):
    image = ImageAuxDataModelSerializer(required=False)

    class Meta:
        model = AboutUsSEODetailsModel
        fields = ('title', 'keywords', 'description', 'image',
                  'type', 'author', 'section', 'published', 'modified')
