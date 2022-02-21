from service.models import ServiceSEODetailsModel
from social_sharing.serializers.image_aux_data import ImageAuxDataModelSerializer
from rest_framework.serializers import ModelSerializer


class RetrieveServiceSEODetailsModelSerializer(ModelSerializer):
    image = ImageAuxDataModelSerializer(required=False)

    class Meta:
        model = ServiceSEODetailsModel
        fields = ('title', 'keywords', 'description', 'image',
                  'type', 'author', 'section', 'published', 'modified')
