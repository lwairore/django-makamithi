from about_us.serializers.ap_about_section import RetrieveApAboutSectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveApAboutSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveApAboutSectionModelSerializer
