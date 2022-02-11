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
