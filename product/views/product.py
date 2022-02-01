from rest_framework.response import Response
from product.serializers.product import ListProductSerializer
from product.submodels.product import ProductModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListProductAPIView(APIView):
    permission_classes = (AllowAny,)
    _category_model_class = ProductModel
    _serializer_class = ListProductSerializer

    def list_product(self):
        categories = self._category_model_class.objects.all()

        return categories

    def get(self, request):
        categories = self.list_product()

        categories_serializer = self._serializer_class(
            categories, many=True)

        return Response(categories_serializer.data)
