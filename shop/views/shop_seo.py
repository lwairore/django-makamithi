from shop.models import ShopSEODetailsModel
from shop.serializers.shop_seo import RetrieveShopSEODetailsModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveShopSEODetailsAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveShopSEODetailsModelSerializer

    def _get_shop_seo_details_instance(self):
        shop_seo_details_instance = ShopSEODetailsModel.objects\
            .select_related('image')\
            .order_by()\
            .only('title', 'keywords', 'description',
                  'image__width', 'image__height', 'image__image', 'image__caption',
                  'type', 'author', 'section', 'published', 'modified')\
            .first()

        return shop_seo_details_instance

    def get(self, request):
        shop_seo_details_instance = self._get_shop_seo_details_instance()

        shop_seo_details_instance_serializer = self._serializer_class(
            shop_seo_details_instance)

        return Response(shop_seo_details_instance_serializer.data)
