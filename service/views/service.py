from rest_framework.response import Response
from service.submodels.service import ServiceModel
from service.serializers.service import (
    RetrieveServiceDetalSerializer,
    RetrieveServiceForAboutPageSerializer,
    RetrieveServiceForHomePageSerializer,
    RetrieveServiceForServicePageSerializer,
    RetrieveServiceForSidebarSectionSerializer)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND


class RetrieveServiceDetailAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceDetalSerializer

    def _get_service_detail_instance(self, service_id: int):
        service_details_kueryset = ServiceModel.objects\
            .only('service_detail_photo__image', 'service_detail_photo__caption',
                  'title', 'description', 'keywords',)\
            .select_related('service_detail_photo')\
            .prefetch_related('plans',)\
            .order_by()\
            .filter(id=service_id)

        if not service_details_kueryset.exists():
            raise ServiceModel.DoesNotExist

        return service_details_kueryset.first()

    def get(self, request, service_id: int):
        service_detail_instance = None

        try:
            service_detail_instance = self._get_service_detail_instance(
                service_id)
        except ServiceModel.DoesNotExist:
            raise Response(
                {'error': f'Service with id "{service_id}" not found.'},
                status=HTTP_404_NOT_FOUND)

        service_detail_instance_serializer = self._serializer_class(
            service_detail_instance)

        return Response(service_detail_instance_serializer.data)


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


class ListServiceForSidebarSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveServiceForSidebarSectionSerializer

    def _list_service(self):
        service_kueryset = ServiceModel.objects\
            .order_by()\
            .only(
                'id',
                'title', )\
            .all()

        return service_kueryset

    def get(self, request):
        service_kueryset = self._list_service()

        service_kueryset_serializer = self._serializer_class(
            service_kueryset, many=True)

        return Response(service_kueryset_serializer.data)
