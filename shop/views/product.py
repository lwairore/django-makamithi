from django.db.models.query import QuerySet
from shop.submodels.product import ProductModel
from shop.submodels.product_category import ProductCategoryModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListProductAPIView(APIView):
    permission_classes = (AllowAny,)

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
            'title', 'flaticon', 'description', 'id')\
            .order_by().all()

        return product_kueryset
