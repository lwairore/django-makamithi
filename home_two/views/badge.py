from rest_framework.response import Response
from django.db.models.query import QuerySet
from home_two.models import BadgeModel
from home_two.serializers.badge import RetrieveBadgeModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListBadgeAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveBadgeModelSerializer

    def _list_badge_kueryset(self):
        badge_kueryset: QuerySet = BadgeModel.objects\
            .order_by().only('number_of_years', 'title',)

        return badge_kueryset

    def get(self, request):
        badge_kueryset = self._list_badge_kueryset()

        badge_kueryset_serializer = self._serializer_class(badge_kueryset,
                                                           many=True)

        return Response(badge_kueryset_serializer.data)
