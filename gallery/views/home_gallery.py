from gallery.submodels.gallery import GalleryModel
from gallery.serializers.home_gallery import ListHomeGallerySerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListHomeGalleryAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = ListHomeGallerySerializer

    def _list_gallery_kueryset(self):
        gallery_kueryset = GalleryModel.objects\
            .only('image__image', 'image__caption',)\
            .select_related('image')\
            .order_by().all()

        return gallery_kueryset
