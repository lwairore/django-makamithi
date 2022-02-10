from rest_framework.response import Response
from home_two.serializers.banner_ad import ListBannerAdModelSerializer
from django.db.models.query import Prefetch
from home_two.submodels.preview_item import PhotoModel
from home_two.submodels.banner_ad import BannerAdModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListBannerAdAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = ListBannerAdModelSerializer

    def _get_banner_ad_kueryset(self):
        photos_kueryset = PhotoModel.objects\
            .order_by().only('image', 'caption',)

        photos_prefetch_related = Prefetch(
            'photos', queryset=photos_kueryset)

        banner_kueryset = BannerAdModel.objects\
            .prefetch_related(photos_prefetch_related)\
            .order_by()\
            .only('title', 'description', 'photos')

        return banner_kueryset

    def get(self, request):
        banner_kueryset = self._get_banner_ad_kueryset()

        banner_kueryset_serializer = self._serializer_class(
            banner_kueryset, many=True)

        return Response(banner_kueryset_serializer.data)
