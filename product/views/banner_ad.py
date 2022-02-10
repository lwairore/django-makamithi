from django.db.models.query import Prefetch
from product.submodels.preview_item import PhotoModel
from product.submodels.banner_ad import BannerAdModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class BannerAdAPIView(APIView):
    permission_classes = (AllowAny,)

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
