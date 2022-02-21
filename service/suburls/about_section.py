from django.urls import path
from custom_utils.get_file_name_util import get_file_name
from service.views.about_section import RetrieveServiceAboutSectionAPIView

SERVICE_ABOUT_SECTION_ROOT_ROUTE = 'retrieve/section/service-about/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_SERVICE_ABOUT_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_SERVICE_ABOUT_SECTION_URL_ROUTE,
        RetrieveServiceAboutSectionAPIView.as_view()
    )
]
