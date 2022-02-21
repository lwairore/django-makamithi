from django.urls import path
from service.views.service_seo import RetrieveServiceSEODetailsAPIView
from custom_utils.get_file_name_util import get_file_name


SERVICE_SEO_DETAILS_ROOT_ROUTE = 'retrieve/seo/service'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_SERVICE_SEO_DETAILS_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_SERVICE_SEO_DETAILS_URL_ROUTE,
        RetrieveServiceSEODetailsAPIView.as_view()
    ),
]
