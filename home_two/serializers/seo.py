from home_two.submodels.seo import HomeSEODetailsModel
from rest_framework.serializers import ModelSerializer


class RetrieveHomeSEODetailsSerializer(ModelSerializer):
    class Meta:
        model = HomeSEODetailsModel
        fields = ('title', 'keywords', 'description', 'image',
                  'url', 'type', 'author', 'section', 'published', 'modified')
