from about_us.submodels.seo import AboutUsSEODetailsModel
from about_us.serializers.seo import RetrieveAboutUsSEODetailsModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveAboutUsSEODetailsAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveAboutUsSEODetailsModelSerializer

    def _get_about_us_seo_details_instance(self):
        about_us_seo_details_instance = AboutUsSEODetailsModel.objects\
            .select_related('image')\
            .order_by()\
            .only('title', 'keywords', 'description',
                  'image__width', 'image__height', 'image__image', 'image__caption',
                  'type', 'author', 'section', 'published', 'modified')\
            .first()

        return about_us_seo_details_instance

    def get(self, request):
        about_us_seo_details_instance = self._get_about_us_seo_details_instance()

        about_us_seo_details_instance_serializer = self._serializer_class(
            about_us_seo_details_instance)

        return Response(about_us_seo_details_instance_serializer.data)
