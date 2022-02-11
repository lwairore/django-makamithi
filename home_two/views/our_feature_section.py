from home_two.submodels.our_feature_section import FeatureSectionModel
from home_two.serializers.our_feature_section import RetrieveFeatureSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveFeatureSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveFeatureSectionSerializer

    def _get_feature_section_instance(self):
        feature_section_instance = FeatureSectionModel.objects\
            .select_related('photo')\
            .order_by()\
            .only('heading', 'description', 'photo__image',
                  'photo__caption').first()

        return feature_section_instance
