from gallery.submodels.gallery import GalleryModel
from gallery.serializers.home_gallery import ListHomeGallerySerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListGalleryForHomePageAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = ListHomeGallerySerializer

    def _list_gallery_kueryset(self):
        gallery_kueryset = GalleryModel.objects\
            .only('home_preview__image', 'home_preview__caption', 'id',)\
            .select_related('home_preview')\
            .order_by().all()

        return gallery_kueryset

    def get(self, request):
        gallery_kueryset = self._list_gallery_kueryset()

        gallery_kueryset_serializer = self._serializer_class(
            gallery_kueryset, many=True)

        return Response(gallery_kueryset_serializer.data)
