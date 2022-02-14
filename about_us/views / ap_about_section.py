from about_us.submodels.ap_about_section import ApAboutSectionModel
from about_us.serializers.ap_about_section import RetrieveApAboutSectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveApAboutSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveApAboutSectionModelSerializer

    def _get_ap_about_section_instance(self):
        ap_about_section_instance = ApAboutSectionModel.objects\
            .only('section_image__image', 'section_image__caption',
                  'heading', 'subheading', 'description',)\
            .select_related('section_image')\
            .order_by()\
            .first()

        return ap_about_section_instance

    def get(self, request):
        ap_about_section_instance = self._get_ap_about_section_instance()

        ap_about_section_instance_serializer = self._serializer_class(
            ap_about_section_instance)

        return Response(ap_about_section_instance_serializer.data)
