from site_breadcrumb.views.site_breadcrumb import RetrieveSiteBreadcrumbModelAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


SITE_BREADCRUMB_ROOT_ROUTE = 'retrieve/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_SITE_BREADCRUMB_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_SITE_BREADCRUMB_URL_ROUTE,
         RetrieveSiteBreadcrumbModelAPIView.as_view()),
]
