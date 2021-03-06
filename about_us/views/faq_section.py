from about_us.submodels.faq_section import FaqSectionModel
from about_us.serializers.faq_section import RetrieveFaqSectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveFaqSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveFaqSectionModelSerializer

    def _get_faq_section_instance(self):
        faq_section_instance = FaqSectionModel.objects\
            .only('heading', 'background_image__image', 'background_image__caption',)\
            .select_related('background_image')\
            .order_by()\
            .first()

        return faq_section_instance

    def get(self, request):
        faq_section_instance = self._get_faq_section_instance()

        faq_section_instance_serializer = self._serializer_class(
            faq_section_instance)

        return Response(faq_section_instance_serializer.data)
