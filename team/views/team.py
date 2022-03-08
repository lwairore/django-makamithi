from custom_utils.pagination import CustomPagination, PaginationHandlerMixin
from rest_framework.response import Response
from django.db.models.query import QuerySet
from team.submodels.team import TeamModel
from team.serializers.team import RetrieveTeamModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListTeamForTeamPageAPIView(APIView, PaginationHandlerMixin):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveTeamModelSerializer
    pagination_class = CustomPagination

    def _list_team_kueryset(self):
        team_kueryset: QuerySet = TeamModel.objects\
            .order_by().only('full_name', 'role', 'image__image',
                             'image__caption', 'facebook', 'twitter',)

        return team_kueryset

    def get(self, request):
        team_kueryset = self._list_team_kueryset()

        results = self.paginate_queryset(team_kueryset)

        team_kueryset_serializer = self._serializer_class(results,
                                                          many=True)

        return self.get_paginated_response(team_kueryset_serializer.data)
