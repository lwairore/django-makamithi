from shop.submodels.product_review import ProductReview
from django.db.models.query import Prefetch, QuerySet
from custom_utils.pagination import CustomPagination, PaginationHandlerMixin
from shop.submodels.product import ProductModel
from shop.serializers.product_review import RetrieveProductReviewSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response


class ListProductReviewAPIView(APIView, PaginationHandlerMixin):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveProductReviewSerializer
    pagination_class = CustomPagination

    def _retrieve_product_instance(self, product_id: int) -> ProductModel:
        product_instance = None

        try:
            review_kueryset = ProductReview.objects\
                .only('full_name', 'client_image__image',
                      'client_image__caption', 'review', 'created_at',
                      'rating',)\
                .select_related('client_image')

            review_pr = Prefetch('reviews', review_kueryset)

            product_instance = ProductModel.objects\
                .only('reviews',)\
                .prefetch_related(review_pr)\
                .get(id=product_id)

        except ProductModel.DoesNotExist as product_does_not_exist:
            raise product_does_not_exist

        return product_instance

    def _list_product_review_kueryset(self, product_instance: ProductModel) -> QuerySet:
        review_kueryset = product_instance.reviews.all()

        return review_kueryset

    def get(self, request, product_id: int):
        pass
        product_instance = None

        try:
            product_instance = self._retrieve_product_instance(
                product_id)
        except ProductModel.DoesNotExist:
            return Response(
                data={
                    'error': f'Product with id {product_id} does not exist'},
                status=HTTP_404_NOT_FOUND)

        review_kueryset = self._list_product_review_kueryset(product_instance)

        results = self.paginate_queryset(review_kueryset)

        results_serializer = self._serializer_class(results, many=True)

        return self.get_paginated_response(results_serializer.data)
