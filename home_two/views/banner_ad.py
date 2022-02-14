from rest_framework.response import Response
from home_two.serializers.banner_ad import ListBannerAdModelSerializer
from django.db.models.query import Prefetch
from home_two.models import PhotoModel
from home_two.submodels.banner_ad import BannerAdModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListBannerAdAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = ListBannerAdModelSerializer

    def _get_banner_ad_kueryset(self):
        banner_kueryset = BannerAdModel.objects\
            .select_related('photo')\
            .order_by()\
            .only('title', 'description', 'photo__image',
                  'photo__caption').all()

        return banner_kueryset

    def get(self, request):
        banner_kueryset = self._get_banner_ad_kueryset()

        banner_kueryset_serializer = self._serializer_class(
            banner_kueryset, many=True)

        return Response(banner_kueryset_serializer.data)
