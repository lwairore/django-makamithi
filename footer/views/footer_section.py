from footer.serializers.footer_section import RetrieveFooterSectionSerializer
from footer.models import FooterSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveFooterSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveFooterSectionSerializer

    def _get_footer_section_instance(self):
        footer_section_instance = FooterSectionModel.objects\
            .only('footer_text', 'footer_logo__image', 'footer_logo__caption',
                  'background_image__image', 'background_image__caption',
                  'section_image__image', 'section_image__caption',)\
            .select_related('footer_logo', 'background_image', 'section_image',)\
            .order_by()\
            .first()

        return footer_section_instance

    def get(self, request):
        footer_section_instance = self._get_footer_section_instance()

        footer_section_instance_serializer = self._serializer_class(
            footer_section_instance)

        return Response(footer_section_instance_serializer.data)
