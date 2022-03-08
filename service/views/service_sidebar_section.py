from service.models import ServiceSidebarSectionModel
from service.serializers.service_sidebar_section import RetrieveServiceSidebarSectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveServiceSidebarSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceSidebarSectionModelSerializer

    def _get_service_sidebar_section_instance(self):
        service_sidebar_section_instance = ServiceSidebarSectionModel.objects\
            .only('background_image__image', 'background_image__caption',
                  'section_image__image', 'section_image__caption',
                  'heading', 'summary',)\
            .select_related('background_image', 'section_image',)\
            .order_by()\
            .first()

        return service_sidebar_section_instance

    def get(self, request):
        service_sidebar_section_instance = self._get_service_sidebar_section_instance()

        service_sidebar_section_instance_serializer = self._serializer_class(
            service_sidebar_section_instance)

        return Response(service_sidebar_section_instance_serializer.data)
