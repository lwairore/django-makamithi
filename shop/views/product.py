from shop.serializers.product import RetrieveProductSerializer
from rest_framework.response import Response
from django.db.models.query import QuerySet
from shop.submodels.product import ProductModel
from shop.submodels.product_category import ProductCategoryModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND


class ListProductAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveProductSerializer

    def _get_product_category_instance(self, product_category_id: int):
        product_category_instance = None

        try:
            product_category_instance = ProductCategoryModel.objects\
                .only('id').get(id=product_category_id)
        except ProductCategoryModel.DoesNotExist as product_category_does_not_exist:
            raise product_category_does_not_exist

        return product_category_instance

    def _list_product_kueryset(self, product_category_id: int) -> QuerySet:
        product_kueryset = ProductModel.objects.only(
            'title', 'id', 'photo__image', 'photo__caption')\
            .order_by()\
            .select_related('photo').filter(category__id=product_category_id)

        return product_kueryset

    def get(self, request, product_category_id: int):
        try:
            self._get_product_category_instance(
                product_category_id=product_category_id)
        except ProductCategoryModel.DoesNotExist:
            return Response(
                data={
                    'error': f'Product category with id {product_category_id} does not exist'},
                status=HTTP_404_NOT_FOUND)

        product_kueryset = self._list_product_kueryset(
            product_category_id=product_category_id)

        product_kueryset_serializer = self._serializer_class(
            product_kueryset, many=True)

        return Response(product_kueryset_serializer.data)
