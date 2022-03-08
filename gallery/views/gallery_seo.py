from gallery.models import GallerySEODetailsModel
from gallery.serializers.gallery_seo import RetrieveGallerySEODetailsModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveGallerySEODetailsAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveGallerySEODetailsModelSerializer

    def _get_gallery_seo_details_instance(self):
        gallery_seo_details_instance = GallerySEODetailsModel.objects\
            .select_related('image')\
            .order_by()\
            .only('title', 'keywords', 'description',
                  'image__width', 'image__height', 'image__image', 'image__caption',
                  'type', 'author', 'section', 'published', 'modified')\
            .first()

        return gallery_seo_details_instance

    def get(self, request):
        gallery_seo_details_instance = self._get_gallery_seo_details_instance()

        gallery_seo_details_instance_serializer = self._serializer_class(
            gallery_seo_details_instance)

        return Response(gallery_seo_details_instance_serializer.data)
