from rest_framework.response import Response
from service.submodels.service import ServiceModel
from service.serializers.service import RetrieveServiceModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListServiceAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceModelSerializer

    def _list_service(self):
        service_kueryset = ServiceModel.objects\
            .select_related('photo')\
            .order_by()\
            .only('photo__image', 'photo__caption', 'id', 'title', 'summary',)\
            .all()

        return service_kueryset

    def get(self, request):
        service_kueryset = self._list_service()

        service_kueryset_serializer = self._serializer_class(service_kueryset)

        return Response(service_kueryset_serializer.data)
