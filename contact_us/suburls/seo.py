from django.urls import path
from contact_us.views.seo import RetrieveContactUsSEODetailsAPIView
from custom_utils.get_file_name_util import get_file_name


CONTACT_US_SEO_DETAILS_ROOT_ROUTE = 'retrieve/seo/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_CONTACT_US_SEO_DETAILS_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_CONTACT_US_SEO_DETAILS_URL_ROUTE,
        RetrieveContactUsSEODetailsAPIView.as_view()
    ),
]
