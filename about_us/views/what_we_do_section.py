from about_us.serializers.what_we_do_section import RetrieveWhatWeDoSectionModelSerializer
from about_us.submodels.what_we_do_section import WhatWeDoSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveWhatWeDoSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveWhatWeDoSectionModelSerializer

    def _get_what_we_do_section_instance(self):
        what_we_do_section_instance = WhatWeDoSectionModel.objects\
            .only('heading', 'section_image__image', 'section_image__caption',
                  'summary',)\
            .select_related('section_image')\
            .order_by()\
            .first()

        return what_we_do_section_instance

    def get(self, request):
        what_we_do_section_instance = self._get_what_we_do_section_instance()

        what_we_do_section_instance_serializer = self._serializer_class(
            what_we_do_section_instance)

        return Response(what_we_do_section_instance_serializer.data)
