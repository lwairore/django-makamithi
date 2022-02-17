from contact_us.submodels.seo import ContactUsSEODetailsModel
from contact_us.serializers.seo import RetrieveContactUsSEODetailsModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveContactUsSEODetailsAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveContactUsSEODetailsModelSerializer

    def _get_contact_us_seo_details_instance(self):
        contact_us_seo_details_instance = ContactUsSEODetailsModel.objects\
            .select_related('image')\
            .order_by()\
            .only('title', 'keywords', 'description',
                  'image__width', 'image__height', 'image__image', 'image__caption',
                  'type', 'author', 'section', 'published', 'modified')\
            .first()

        return contact_us_seo_details_instance

    def get(self, request):
        contact_us_seo_details_instance = self._get_contact_us_seo_details_instance()

        contact_us_seo_details_instance_serializer = self._serializer_class(
            contact_us_seo_details_instance)

        return Response(contact_us_seo_details_instance_serializer.data)
