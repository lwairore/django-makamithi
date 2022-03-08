from contact_us.submodels.leave_us_a_message_section import LeaveUsAMessageSectionModel
from contact_us.serializers.leave_us_a_message_section import RetrieveLeaveUsAMessageSectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveLeaveUsAMessageSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveLeaveUsAMessageSectionModelSerializer

    def _get_leave_us_a_message_section_instance(self):
        leave_us_a_message_section_instance = LeaveUsAMessageSectionModel.objects\
            .only('heading', 'background_image__image', 'background_image__caption',
                  'summary', 'our_promise',)\
            .select_related('background_image')\
            .order_by()\
            .first()

        return leave_us_a_message_section_instance

    def get(self, request):
        leave_us_a_message_section_instance = self._get_leave_us_a_message_section_instance()

        leave_us_a_message_section_instance_serializer = self._serializer_class(
            leave_us_a_message_section_instance)

        return Response(leave_us_a_message_section_instance_serializer.data)
