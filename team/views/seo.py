from team.submodels.seo import TeamSEODetailsModel
from team.serializers.seo import RetrieveTeamSEODetailsModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveTeamSEODetailsAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveTeamSEODetailsModelSerializer

    def _get_team_seo_details_instance(self):
        team_seo_details_instance = TeamSEODetailsModel.objects\
            .select_related('image')\
            .order_by()\
            .only('title', 'keywords', 'description',
                  'image__width', 'image__height', 'image__image', 'image__caption',
                  'type', 'author', 'section', 'published', 'modified')\
            .first()

        return team_seo_details_instance

    def get(self, request):
        team_seo_details_instance = self._get_team_seo_details_instance()

        team_seo_details_instance_serializer = self._serializer_class(
            team_seo_details_instance)

        return Response(team_seo_details_instance_serializer.data)
