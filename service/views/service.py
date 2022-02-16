from rest_framework.response import Response
from service.submodels.service import ServiceModel
from service.serializers.service import RetrieveAboutServiceModelSerializer, RetrieveHomeServiceModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListHomeServiceAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveHomeServiceModelSerializer

    def _list_service(self):
        service_kueryset = ServiceModel.objects\
            .select_related('home_photo')\
            .order_by()\
            .only('home_photo__image', 'home_photo__caption', 'id', 'title', 'summary',)\
            .all()

        return service_kueryset

    def get(self, request):
        service_kueryset = self._list_service()

        service_kueryset_serializer = self._serializer_class(
            service_kueryset, many=True)

        return Response(service_kueryset_serializer.data)


class ListAboutServiceAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveAboutServiceModelSerializer

    def _list_service(self):
        service_kueryset = ServiceModel.objects\
            .select_related('about_photo')\
            .order_by()\
            .only('about_photo__image', 'about_photo__caption', 'id', 'title', 'summary',)\
            .all()

        return service_kueryset

    def get(self, request):
        service_kueryset = self._list_service()

        service_kueryset_serializer = self._serializer_class(
            service_kueryset, many=True)

        return Response(service_kueryset_serializer.data)
