from home_two.submodels.counter_area_section import CounterAreaSectionModel
from rest_framework.response import Response
from home_two.serializers.counter_area_section import RetrieveCounterAreaSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveCounterAreaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveCounterAreaSectionSerializer

    def _get_counter_area_section_instance(self):
        counter_area_section_instance = CounterAreaSectionModel.objects\
            .order_by()\
            .only('heading', 'background_image',).first()

        return counter_area_section_instance

    def get(self, request):
        counter_area_section_instance = self._get_counter_area_section_instance()

        counter_area_section_instance_serializer = self._serializer_class(
            counter_area_section_instance)

        return Response(counter_area_section_instance_serializer.data)
