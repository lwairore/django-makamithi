from django.urls import path
from custom_utils.get_file_name_util import get_file_name
from service.views.service_sidebar_section import RetrieveServiceSidebarSectionAPIView

SERVICE_SIDEBAR_SECTION_ROOT_ROUTE = 'retrieve/section/service-sidebar/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_SERVICE_SIDEBAR_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_SERVICE_SIDEBAR_SECTION_URL_ROUTE,
        RetrieveServiceSidebarSectionAPIView.as_view()
    )
]
