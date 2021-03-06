from home_two.submodels.gallery_section import GallerySectionModel
from home_two.serializers.gallery_section import RetrieveGallerySectionModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveGallerySectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveGallerySectionModelSerializer

    def _get_gallery_section_instance(self):
        gallery_section_instance = GallerySectionModel.objects\
            .select_related('section_image')\
            .order_by()\
            .only('heading', 'summary', 'section_image__image',
                  'section_image__caption',
                  'background_image__image',
                  'background_image__caption',)\
            .first()

        return gallery_section_instance

    def get(self, request):
        gallery_section_instance = self._get_gallery_section_instance()

        gallery_section_instance_serializer = self._serializer_class(
            gallery_section_instance)

        return Response(gallery_section_instance_serializer.data)
