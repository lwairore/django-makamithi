from gallery.serializers.home_gallery import ListHomeGallerySerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListHomeGalleryAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = ListHomeGallerySerializer