from home_two.serializers.gallery_section import RetrieveGallerySectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveGallerySectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveGallerySectionModelSerializer