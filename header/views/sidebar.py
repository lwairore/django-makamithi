from contact_us.submodels.contact_info import ContactInfoModel
from header.serializers.sidebar import RetrieveContactInfoModelSerializer, RetrieveServiceForSidebarSerializer
from service.submodels.service import ServiceModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class ListContactInfoAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveContactInfoModelSerializer

    def _list_contact_info_kueryset(self):
        contact_info_kueryset = ContactInfoModel.objects\
            .order_by()\
            .only('address_title',
                  'address',
                  'email',
                  'phone_number',)\
            .all()

        return contact_info_kueryset

    def get(self, request):
        contact_info_kueryset = self._list_contact_info_kueryset()

        contact_info_kueryset_serializer = self._serializer_class(
            contact_info_kueryset, many=True)

        return Response(contact_info_kueryset_serializer.data)


class ListServicePageAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceForSidebarSerializer

    def _list_service(self):
        service_kueryset = ServiceModel.objects\
            .select_related('nav_sidebar_photo')\
            .order_by()\
            .only('nav_sidebar_photo__image', 'nav_sidebar_photo__caption', 'id', 'title', )\
            .all()

        return service_kueryset

    def get(self, request):
        service_kueryset = self._list_service()

        service_kueryset_serializer = self._serializer_class(
            service_kueryset, many=True)

        return Response(service_kueryset_serializer.data)
