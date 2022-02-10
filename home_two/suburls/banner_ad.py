from home_two.views.banner_ad import ListBannerAdAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

BANNER_AD_ROOT_ROUTE = 'list/banner-ad/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_BANNER_AD_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_BANNER_AD_URL_ROUTE, ListBannerAdAPIView.as_view()),
]
