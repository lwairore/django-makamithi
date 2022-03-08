from custom_utils.iterable_object_is_not_empty import iterable_object_is_not_empty
from inbox.serializers.inbox import AddNewMessageModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED


class AddNewMessageAPIView(APIView):
    permission_classes = (AllowAny, )
    _serializer_class = AddNewMessageModelSerializer

    def post(self, request):
        new_message_details = self._serializer_class\
            .format_request_data(request.data)

        if not iterable_object_is_not_empty(new_message_details):
            return Response(data={'error': 'Details cannot be empty'},
                            status=HTTP_400_BAD_REQUEST)

        new_message_serializer = self._serializer_class(
            data=new_message_details)
        if new_message_serializer.is_valid():
            new_message_serializer.save()

            return Response(
                data={'details': 'Message successfully received'},
                status=HTTP_201_CREATED)
        return Response(new_message_serializer.errors,
                        status=HTTP_400_BAD_REQUEST)
