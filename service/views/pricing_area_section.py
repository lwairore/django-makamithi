from service.serializers.pricing_area_section import RetrievePricingAreaSectionModelSerializer
from service.submodels.pricing_area_section import PricingAreaSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrievePricingAreaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrievePricingAreaSectionModelSerializer

    def _get_pricing_area_section_instance(self):
        pricing_area_section_instance = PricingAreaSectionModel.objects\
            .only('heading', 'section_image__image', 'section_image__caption',
                  'summary',)\
            .select_related('section_image')\
            .order_by()\
            .first()

        return pricing_area_section_instance

    def get(self, request):
        pricing_area_section_instance = self._get_pricing_area_section_instance()

        pricing_area_section_instance_serializer = self._serializer_class(
            pricing_area_section_instance)

        return Response(pricing_area_section_instance_serializer.data)
