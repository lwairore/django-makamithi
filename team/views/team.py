from rest_framework.response import Response
from django.db.models.query import QuerySet
from team.submodels.team import TeamModel
from team.serializers.team import RetrieveTeamModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListTeamAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveTeamModelSerializer

    def _list_team_kueryset(self):
        team_kueryset: QuerySet = TeamModel.objects\
            .order_by().only('full_name', 'role', 'image__image',
                             'image__caption', 'facebook', 'twitter',)

        return team_kueryset

    def get(self, request):
        team_kueryset = self._list_team_kueryset()

        team_kueryset_serializer = self._serializer_class(team_kueryset,
                                                          many=True)

        return Response(team_kueryset_serializer.data)
