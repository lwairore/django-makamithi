from rest_framework.response import Response
from home_two.serializers.visit_now_cta_section import RetrieveVisitNowCtaSectionSerializer
from home_two.submodels.visit_now_cta_section import VisitNowCtaSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveVisitNowCtaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveVisitNowCtaSectionSerializer

    def _get_visit_now_cta_section_instance(self):
        visit_now_cta_section_instance = VisitNowCtaSectionModel.objects\
            .select_related('background_image', 'section_image',)\
            .order_by()\
            .only('heading', 'description', 'section_image__image',
                  'section_image__caption',
                  'background_image__image',
                  'background_image__caption').first()

        return visit_now_cta_section_instance

    def get(self, request):
        visit_now_cta_section_instance = self._get_visit_now_cta_section_instance()

        visit_now_cta_section_instance_serializer = self._serializer_class(
            visit_now_cta_section_instance)

        return Response(visit_now_cta_section_instance_serializer.data)
