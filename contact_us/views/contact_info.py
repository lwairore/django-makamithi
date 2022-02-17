from contact_us.serializers.contact_info import RetrieveContactInfoModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListContactInfoAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveContactInfoModelSerializer
