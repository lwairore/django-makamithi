from rest_framework.response import Response
from home_two.submodels.our_feature_section import FeatureSectionModel
from home_two.serializers.our_feature_section import RetrieveFeatureSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveFeatureSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveFeatureSectionSerializer

    def _get_feature_section_instance(self):
        feature_section_instance = FeatureSectionModel.objects\
            .select_related('photo', 'background_image', 'section_image',)\
            .order_by()\
            .only('summary', 'section_image__image',
                  'section_image__caption',
                  'background_image__image',
                  'background_image__caption').first()

        return feature_section_instance

    def get(self, request):
        feature_section_instance = self._get_feature_section_instance()

        feature_section_instance_serializer = self._serializer_class(
            feature_section_instance)

        return Response(feature_section_instance_serializer.data)
