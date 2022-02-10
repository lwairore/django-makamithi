from rest_framework.response import Response
from home_two.submodels.about_section import AboutSectionModel
from home_two.serializers.about_section import RetrieveAboutSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveAboutSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveAboutSectionSerializer

    def _get_about_section_instance(self):
        about_section_instance = AboutSectionModel.objects\
            .select_related('photo')\
            .order_by()\
            .only('heading', 'subheading', 'description', 'photo__image',
                  'photo__caption').first()

        return about_section_instance

    def get(self, request):
        about_section_instance = self._get_about_section_instance()

        about_section_instance_serializer = self._serializer_class(
            about_section_instance)

        return Response(about_section_instance_serializer.data)
