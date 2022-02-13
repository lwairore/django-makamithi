from rest_framework.response import Response
from django.db.models.query import QuerySet
from home_two.submodels.core_value import CoreValueModel
from home_two.serializers.core_value import CoreValueModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class CoreValueAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = CoreValueModelSerializer

    def _list_core_value_kueryset(self):
        core_value_kueryset: QuerySet = CoreValueModel.objects\
            .order_by().only('title', 'description', 'image__image',
                             'image__caption', 'id',)

        return core_value_kueryset

    def get(self, request):
        core_value_kueryset = self._list_core_value_kueryset()

        core_value_kueryset_serializer = self._serializer_class(core_value_kueryset,
                                                                many=True)

        return Response(core_value_kueryset_serializer.data)
