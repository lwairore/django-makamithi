from rest_framework.response import Response
from service.submodels.service import ServiceModel
from service.serializers.service import (
    RetrieveServiceForAboutPageSerializer,
    RetrieveServiceForHomePageSerializer,
    RetrieveServiceForServicePageSerializer)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListServiceForHomePageAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceForHomePageSerializer

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


class ListServiceForAboutPageAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceForAboutPageSerializer

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


class ListServiceForServicePageAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceForServicePageSerializer

    def _list_service(self):
        service_kueryset = ServiceModel.objects\
            .select_related('service_page_photo')\
            .order_by()\
            .only(
                'service_page_photo__image',
                'service_page_photo__caption',
                'id',
                'title',
                'summary',)\
            .all()

        return service_kueryset

    def get(self, request):
        service_kueryset = self._list_service()

        service_kueryset_serializer = self._serializer_class(
            service_kueryset, many=True)

        return Response(service_kueryset_serializer.data)
