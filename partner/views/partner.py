from partner.models import PartnerModel
from partner.serializers.partner import RetrievePartnerModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListPartnerModelAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrievePartnerModelSerializer

    def _list_partner_kueryset(self):
        partner_kueryset = PartnerModel.objects\
            .order_by()\
            .only('title', 'link', 'image')\
            .all()

        return partner_kueryset

    def get(self, request):
        partner_kueryset = self._list_partner_kueryset()

        partner_kueryset_serializer = self._serializer_class(
            partner_kueryset, many=True)

        return Response(partner_kueryset_serializer.data)
