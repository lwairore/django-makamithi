from partner.models import PartnerAreaSectionModel
from partner.serializers.partner_area_section import RetrievePartnerAreaSectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrievePartnerAreaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrievePartnerAreaSectionModelSerializer

    def _get_partner_area_section_instance(self):
        partner_area_section_instance = PartnerAreaSectionModel.objects\
            .only('background_image__image', 'background_image__caption',
                  )\
            .select_related('background_image')\
            .order_by()\
            .first()

        return partner_area_section_instance

    def get(self, request):
        partner_area_section_instance = self._get_partner_area_section_instance()

        partner_area_section_instance_serializer = self._serializer_class(
            partner_area_section_instance)

        return Response(partner_area_section_instance_serializer.data)
