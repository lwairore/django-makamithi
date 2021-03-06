from home_two.submodels.seo import HomeSEODetailsModel
from home_two.serializers.seo import RetrieveHomeSEODetailsSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveHomeSEODetailsAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveHomeSEODetailsSerializer

    def _get_home_seo_details_instance(self):
        home_seo_details_instance = HomeSEODetailsModel.objects\
            .select_related('image')\
            .order_by()\
            .only('title', 'keywords', 'description',
                  'image__width', 'image__height', 'image__image', 'image__caption',
                  'type', 'author', 'section', 'published', 'modified')\
            .first()

        return home_seo_details_instance

    def get(self, request):
        home_seo_details_instance = self._get_home_seo_details_instance()

        home_seo_details_instance_serializer = self._serializer_class(
            home_seo_details_instance)

        return Response(home_seo_details_instance_serializer.data)
