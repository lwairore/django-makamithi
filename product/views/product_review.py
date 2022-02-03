from django.db.models.query import Prefetch
from product.submodels.product import ProductModel
from product.submodels.rating_scale import FivePointRatingScaleModel, RatingScaleModel
from product.serializers.product_review import ListProductReviewSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView

class UpdateDeleteProductReview(APIView):
    permission_classes = (AllowAny,)
    

class ListProductReviewAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = ListProductReviewSerializer

    def _get_product_instance(self, product_id: int):
        product_instance = None

        try:
            star_kueryset = RatingScaleModel.objects.order_by()

            five_star_prefetch_related = Prefetch(
                'five_star', queryset=star_kueryset)
            four_star_prefetch_related = Prefetch(
                'four_star', queryset=star_kueryset)
            three_star_prefetch_related = Prefetch(
                'three_star', queryset=star_kueryset)
            two_star_prefetch_related = Prefetch(
                'two_star', queryset=star_kueryset)
            one_star_prefetch_related = Prefetch(
                'one_star', queryset=star_kueryset)

            reviews_kueryset = FivePointRatingScaleModel.objects\
                .order_by().prefetch_related(
                    five_star_prefetch_related,
                    four_star_prefetch_related,
                    three_star_prefetch_related, two_star_prefetch_related, one_star_prefetch_related)

            reviews_prefetch_related = Prefetch(
                'reviews', queryset=reviews_kueryset)

            product_instance = ProductModel.objects\
                .prefetch_related(reviews_prefetch_related).get(id=product_id)

            return product_instance

        except ProductModel.DoesNotExist as product_does_not_exist:
            raise product_does_not_exist

    def _list_reviews(self, product_instance: ProductModel):
        reviews = product_instance.reviews.order_by().all()

        return reviews

    def get(self, request, product_id: int):
        product_instance = None

        try:
            product_instance = self._get_product_instance(product_id)

        except ProductModel.DoesNotExist:
            return Response({'detail': f'Product with that id {product_id} not found.'}, status=HTTP_404_NOT_FOUND)

        reviews = self._list_reviews(product_instance)

        reviews_serializer = self._serializer_class(reviews, many=True)

        return Response(reviews_serializer.data)
