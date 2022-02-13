from gallery.submodels.gallery import GalleryModel
from rest_framework.serializers import ModelSerializer

class ListHomeGallerySerializer(ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = ('image',)