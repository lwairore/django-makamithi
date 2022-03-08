from django.urls import path
from shop.views.shop_seo import RetrieveShopSEODetailsAPIView
from custom_utils.get_file_name_util import get_file_name


SHOP_SEO_DETAILS_ROOT_ROUTE = 'retrieve/seo/shop/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_SHOP_SEO_DETAILS_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_SHOP_SEO_DETAILS_URL_ROUTE,
        RetrieveShopSEODetailsAPIView.as_view()
    ),
]
