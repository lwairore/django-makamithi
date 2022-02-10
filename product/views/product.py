from django.db.models.query import Prefetch
from product.submodels.rating_scale import ProductReviewModel
from rest_framework.response import Response
from product.serializers.product import ListProductSerializer
from product.submodels.product import ProductModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveProductAPIView(APIView):
    permission_classes = (AllowAny,)

    def _get_product_instance(self, product_id: int):
        product_instance = None

        try:
            reviews_kueryset = ProductReviewModel.objects\
                .order_by()

            reviews_prefetch_related = Prefetch(
                'reviews', queryset=reviews_kueryset)

            product_instance = ProductModel.objects\
                .prefetch_related(reviews_prefetch_related).get(id=product_id)

            return product_instance

        except ProductModel.DoesNotExist as product_does_not_exist:
            raise product_does_not_exist

    def get(self, request, product_id: int):
        product_instance = None

        try:
            product_instance = self._get_product_instance(product_id)

        except ProductModel.DoesNotExist:
            return Response({'detail': f'Product with that id {product_id} not found.'}, status=HTTP_404_NOT_FOUND)
            


class ListProductAPIView(APIView):
    permission_classes = (AllowAny,)
    _category_model_class = ProductModel
    _serializer_class = ListProductSerializer

    def list_product(self):
        categories = self._category_model_class.objects\
            .select_related('category').all()

        return categories

    def get(self, request):
        categories = self.list_product()

        categories_serializer = self._serializer_class(
            categories, many=True)

        return Response(categories_serializer.data)
