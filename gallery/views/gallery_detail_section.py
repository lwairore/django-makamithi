from gallery.serializers.gallery_detail_section import RetrieveGalleryDetailSectionModelSerializer
from gallery.submodels.gallery_detail_section import GalleryDetailSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveGalleryDetailSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveGalleryDetailSectionModelSerializer

    def _get_gallery_detail_section_instance(self):
        gallery_detail_section_instance = GalleryDetailSectionModel.objects\
            .only('background_image__image', 'background_image__caption',)\
            .select_related('background_image')\
            .order_by()\
            .first()

        return gallery_detail_section_instance

    def get(self, request):
        gallery_detail_section_instance = self._get_gallery_detail_section_instance()

        gallery_detail_section_instance_serializer = self._serializer_class(
            gallery_detail_section_instance)

        return Response(gallery_detail_section_instance_serializer.data)
