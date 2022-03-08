from shop.models import ShopSEODetailsModel
from social_sharing.serializers.image_aux_data import ImageAuxDataModelSerializer
from rest_framework.serializers import ModelSerializer


class RetrieveShopSEODetailsModelSerializer(ModelSerializer):
    image = ImageAuxDataModelSerializer(required=False)

    class Meta:
        model = ShopSEODetailsModel
        fields = ('title', 'keywords', 'description', 'image',
                  'type', 'author', 'section', 'published', 'modified')
