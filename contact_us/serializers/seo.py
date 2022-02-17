from contact_us.models import ContactUsSEODetailsModel
from social_sharing.serializers.image_aux_data import ImageAuxDataModelSerializer
from rest_framework.serializers import ModelSerializer


class RetrieveContactUsSEODetailsModelSerializer(ModelSerializer):
    image = ImageAuxDataModelSerializer(required=False)

    class Meta:
        model = ContactUsSEODetailsModel
        fields = ('title', 'keywords', 'description', 'image',
                  'type', 'author', 'section', 'published', 'modified')
