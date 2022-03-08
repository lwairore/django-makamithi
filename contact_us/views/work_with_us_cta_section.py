from rest_framework.response import Response
from contact_us.serializers.work_with_us_cta_section import RetrieveWorkWithUsCtaSectionSerializer
from contact_us.submodels.work_with_us_cta_section import WorkWithUsCtaSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveWorkWithUsCtaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveWorkWithUsCtaSectionSerializer

    def _get_work_with_us_cta_section_instance(self):
        work_with_us_cta_section_instance = WorkWithUsCtaSectionModel.objects\
            .select_related('background_image', 'section_image',)\
            .order_by()\
            .only('heading', 'description', 'section_image__image',
                  'section_image__caption', 'call_to_action',
                  'background_image__image',
                  'background_image__caption').first()

        return work_with_us_cta_section_instance

    def get(self, request):
        work_with_us_cta_section_instance = self._get_work_with_us_cta_section_instance()

        work_with_us_cta_section_instance_serializer = self._serializer_class(
            work_with_us_cta_section_instance)

        return Response(work_with_us_cta_section_instance_serializer.data)
