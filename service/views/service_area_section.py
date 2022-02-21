from service.models import ServiceAreaSectionModel
from service.serializers.service_area_section import RetrieveServiceAreaSectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveServiceAreaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceAreaSectionModelSerializer

    def _get_service_area_section_instance(self):
        service_area_section_instance = ServiceAreaSectionModel.objects\
            .only('years_of_experience_image__image', 'years_of_experience_image__caption',
                  'heading', 'description',)\
            .select_related('years_of_experience_image')\
            .order_by()\
            .first()

        return service_area_section_instance

    def get(self, request):
        service_area_section_instance = self._get_service_area_section_instance()

        service_area_section_instance_serializer = self._serializer_class(
            service_area_section_instance)

        return Response(service_area_section_instance_serializer.data)
