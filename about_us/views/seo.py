from about_us.serializers.seo import RetrieveAboutUsSEODetailsModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveAboutUsSEODetailsAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveAboutUsSEODetailsModelSerializer
