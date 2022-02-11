from shop.submodels.product_category import ProductCategoryModel
from shop.serializers.product_category import RetrieveProductCategorySerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListProductCategoryAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveProductCategorySerializer

    def _list_product_category_kueryset(self):
        product_category_kueryset = ProductCategoryModel.objects\
            .only('title', 'flaticon', 'description', 'id',).order_by()\
            .all()

        return product_category_kueryset
