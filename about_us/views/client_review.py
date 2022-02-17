from about_us.models import ClientReviewModel
from about_us.serializers.client_review import RetrieveClientReviewModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListClientReviewModelAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveClientReviewModelSerializer

    def _list_client_review_kueryset(self):
        client_review_kueryset = ClientReviewModel.objects\
            .order_by()\
            .only(
                'full_name', 'review',
                'image__image', 'image__caption', )\
            .all()

        return client_review_kueryset

    def get(self, request):
        client_review_kueryset = self._list_client_review_kueryset()

        client_review_kueryset_serializer = self._serializer_class(
            client_review_kueryset, many=True)

        return Response(client_review_kueryset_serializer.data)
