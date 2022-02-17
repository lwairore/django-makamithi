from about_us.serializers.team_area_section import RetrieveTeamAreaSectionModelSerializer
from about_us.submodels.team_area_section import TeamAreaSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveTeamAreaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveTeamAreaSectionModelSerializer

    def _get_team_area_section_instance(self):
        team_area_section_instance = TeamAreaSectionModel.objects\
            .only('heading', 'section_image__image', 'section_image__caption',
                  'summary',)\
            .select_related('section_image')\
            .order_by()\
            .first()

        return team_area_section_instance

    def get(self, request):
        team_area_section_instance = self._get_team_area_section_instance()

        team_area_section_instance_serializer = self._serializer_class(
            team_area_section_instance)

        return Response(team_area_section_instance_serializer.data)
