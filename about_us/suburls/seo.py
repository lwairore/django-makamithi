from django.urls import path
from about_us.views.seo import RetrieveAboutUsSEODetailsAPIView
from custom_utils.get_file_name_util import get_file_name


ABOUT_US_SEO_DETAILS_ROOT_ROUTE = 'retrieve/seo/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_ABOUT_US_SEO_DETAILS_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_ABOUT_US_SEO_DETAILS_URL_ROUTE,
        RetrieveAboutUsSEODetailsAPIView.as_view()
    ),
]
