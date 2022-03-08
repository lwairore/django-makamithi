from custom_utils.pagination import CustomPagination, PaginationHandlerMixin
from shop.serializers.product import RetrieveProductDetailSerializer, RetrieveProductSerializer
from rest_framework.response import Response
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from shop.submodels.product import ProductModel
from shop.submodels.product_category import ProductCategoryModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND


class RetrieveProductDetailAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveProductDetailSerializer

    def _retrieve_product_instance(self, product_id: int) -> ProductModel:
        product_instance = None

        try:
            product_instance = ProductModel.objects\
                .only('title', 'keywords', 'total_sales', 'description',
                      'price__was', 'price__now', 'created_at', 'modified_date')\
                .prefetch_related('product_images',
                                  'reviews',)\
                .select_related('price',)\
                .annotate(
                    total_reviews=Count('reviews', distinct=True))\
                .get(id=product_id)
        except ProductModel.DoesNotExist as product_does_not_exist:
            raise product_does_not_exist

        return product_instance

    def get(self, request, product_id: int):
        product_instance = None

        try:
            product_instance = self._retrieve_product_instance(
                product_id)
        except ProductModel.DoesNotExist:
            return Response(
                data={
                    'error': f'Product with id {product_id} does not exist'},
                status=HTTP_404_NOT_FOUND)

        product_instance_serializer = self._serializer_class(product_instance)

        return Response(product_instance_serializer.data)


class ListProductForShopPageAPIView(APIView, PaginationHandlerMixin):
    permission_classes = (AllowAny, )
    _serializer_class = RetrieveProductSerializer
    pagination_class = CustomPagination

    def _list_product_kueryset(self) -> QuerySet:
        product_kueryset = ProductModel.objects.only(
            'title', 'id', 'product_preview__image', 'product_preview__caption', 'price__now',
            'total_sales',
        )\
            .order_by()\
            .select_related('product_preview', 'price',)\
            .all()

        return product_kueryset

    def get(self, request):
        product_kueryset = self._list_product_kueryset()

        results = self.paginate_queryset(product_kueryset)

        product_kueryset_serializer = self._serializer_class(
            results, many=True)

        return self.get_paginated_response(product_kueryset_serializer.data)


class ListProductForHomePageAPIView(APIView):
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
            'title', 'id', 'product_preview__image', 'product_preview__caption', 'price__now',
            'total_sales',
        )\
            .order_by()\
            .select_related('product_preview', 'price',).filter(category__id=product_category_id)

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
