from home_two.submodels.visit_now_cta_section import VisitNowCtaSectionModel
from rest_framework.serializers import ModelSerializer


class RetrieveVisitNowCtaSectionSerializer(ModelSerializer):
    class Meta:
        model = VisitNowCtaSectionModel
        fields = ('heading', 'description',
                  'background_image', 'section_image',)
