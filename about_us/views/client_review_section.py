from about_us.serializers.client_review_section import RetrieveClientReviewSectionModelSerializer
from about_us.submodels.client_review_section import ClientReviewSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveClientReviewSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveClientReviewSectionModelSerializer

    def _get_client_review_section_instance(self):
        client_review_section_instance = ClientReviewSectionModel.objects\
            .only('heading', 'section_image__image', 'section_image__caption',
                  'background_image__image', 'background_image__caption',
                  'summary',)\
            .select_related('section_image', 'background_image',)\
            .order_by()\
            .first()

        return client_review_section_instance

    def get(self, request):
        client_review_section_instance = self._get_client_review_section_instance()

        client_review_section_instance_serializer = self._serializer_class(
            client_review_section_instance)

        return Response(client_review_section_instance_serializer.data)
