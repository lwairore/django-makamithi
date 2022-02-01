from product.serializers import ListProductCategorySerializer
from product.submodels.category import ProductCategoryModel
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListProductCategoryAPIView(APIView):
    permission_classes = (AllowAny,)
    _category_model_class = ProductCategoryModel
    _serializer_class = ListProductCategorySerializer

    def list_product_category(self):
        categories = self._category_model_class.objects.all()

        return categories

    def get(self, request):
        categories = self.list_product_category()

        categories_serializer = self._serializer_class(
            categories, many=True)

        return Response(categories_serializer.data)
