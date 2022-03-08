from header.serializers.header_section import RetrieveHeaderSectionForTopHeaderModelSerializer, RetrieveLogosForStickyHeaderSectionSerializer
from header.submodels.header_section import HeaderSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveHeaderSectionForTopHeaderAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveHeaderSectionForTopHeaderModelSerializer

    def _get_header_section_instance(self):
        header_section_instance = HeaderSectionModel.objects\
            .only('primary_location', 'whatsapp_business_number',)\
            .order_by()\
            .first()

        return header_section_instance

    def get(self, request):
        header_section_instance = self._get_header_section_instance()

        header_section_instance_serializer = self._serializer_class(
            header_section_instance)

        return Response(header_section_instance_serializer.data)


class RetrieveLogosForStickyHeaderSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveLogosForStickyHeaderSectionSerializer

    def _get_header_section_instance(self):
        header_section_instance = HeaderSectionModel.objects\
            .only('standard_logo__image', 'standard_logo__caption', 'retina_logo__image', 'retina_logo__caption')\
            .select_related('standard_logo', 'retina_logo',)\
            .order_by()\
            .first()

        return header_section_instance

    def get(self, request):
        header_section_instance = self._get_header_section_instance()

        header_section_instance_serializer = self._serializer_class(
            header_section_instance)

        return Response(header_section_instance_serializer.data)
