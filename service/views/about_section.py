from service.models import ServiceAboutSectionModel
from service.serializers.about_section import RetrieveServiceAboutSectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveServiceAboutSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceAboutSectionModelSerializer

    def _get_service_about_section_instance(self):
        service_about_section_instance = ServiceAboutSectionModel.objects\
            .only('section_image__image', 'section_image__caption',
                  'heading', 'description',)\
            .select_related('section_image')\
            .order_by()\
            .first()

        return service_about_section_instance

    def get(self, request):
        service_about_section_instance = self._get_service_about_section_instance()

        service_about_section_instance_serializer = self._serializer_class(
            service_about_section_instance)

        return Response(service_about_section_instance_serializer.data)
