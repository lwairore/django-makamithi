from home_two.submodels import GallerySectionModel
from rest_framework.serializers import ModelSerializer


class RetrieveGallerySectionModelSerializer(ModelSerializer):
    class Meta:
        model = GallerySectionModel
        fields = ('heading', 'summary', 'section_image',)
