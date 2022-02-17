from contact_us.submodels.contact_info import ContactInfoModel
from contact_us.serializers.contact_info import RetrieveContactInfoModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListContactInfoAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveContactInfoModelSerializer

    def _list_contact_info_kueryset(self):
        contact_info_kueryset = ContactInfoModel.objects\
            .order_by()\
            .only('question', 'answer',)\
            .all()

        return contact_info_kueryset

    def get(self, request):
        contact_info_kueryset = self._list_contact_info_kueryset()

        contact_info_kueryset_serializer = self._serializer_class(
            contact_info_kueryset, many=True)

        return Response(contact_info_kueryset_serializer.data)
