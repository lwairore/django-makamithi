from home_two.views.seo import RetrieveHomeSEODetailsAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


HOME_SEO_DETAILS_ROOT_ROUTE = 'retrieve/seo/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_HOME_SEO_DETAILS_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_HOME_SEO_DETAILS_URL_ROUTE,
         RetrieveHomeSEODetailsAPIView.as_view())
]
