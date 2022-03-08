from header.views.sidebar import ListContactInfoAPIView, ListServicePageAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

SIDEBAR_ROOT_ROUTE = 'nav/sidebar/'

_LIST_SERVICE_ROUTE = 'list/service/'

_LIST_CONTACT_INFO_URL_ROUTE = 'list/contact-info/'


urlpatterns = [
    # Service for service nav sidebar
    path(_LIST_SERVICE_ROUTE,
         ListServicePageAPIView.as_view()),

    # URLConf for 'Contact info' for nav sidebar
    path(_LIST_CONTACT_INFO_URL_ROUTE,
         ListContactInfoAPIView.as_view()),
]
