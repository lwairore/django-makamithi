from service.models import ServiceSEODetailsModel
from service.serializers.service_seo import RetrieveServiceSEODetailsModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveServiceSEODetailsAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceSEODetailsModelSerializer

    def _get_service_seo_details_instance(self):
        service_seo_details_instance = ServiceSEODetailsModel.objects\
            .select_related('image')\
            .order_by()\
            .only('title', 'keywords', 'description',
                  'image__width', 'image__height', 'image__image', 'image__caption',
                  'type', 'author', 'section', 'published', 'modified')\
            .first()

        return service_seo_details_instance

    def get(self, request):
        service_seo_details_instance = self._get_service_seo_details_instance()

        service_seo_details_instance_serializer = self._serializer_class(
            service_seo_details_instance)

        return Response(service_seo_details_instance_serializer.data)
