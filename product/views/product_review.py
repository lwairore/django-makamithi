from product.submodels.rating_scale import FivePointRatingScaleModel
from product.serializers.product_review import ListProductReviewSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class ListProductReviewAPIView(APIView):
    permission_classes = (IsAuthenticated)
    _serializer_class = ListProductReviewSerializer

    def _list_reviews(self):
        reviews = FivePointRatingScaleModel.objects.order_by().all()

        return reviews

    def get(self, request):
        reviews = self._list_reviews()

        reviews_serializer = self._serializer_class(reviews, many=True)

        return Response(reviews_serializer.data)
