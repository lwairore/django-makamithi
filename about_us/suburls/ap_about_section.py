from django.urls.conf import path
from custom_utils.get_file_name_util import get_file_name
from about_us.views.ap_about_section import RetrieveApAboutSectionAPIView

AP_ABOUT_SECTION_ROOT_ROUTE = 'retrieve/section/ap-about/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_API_ABOUT_SECTION_URL_ROUTE = ''

urpatterns = [
    path(
        _RETRIEVE_API_ABOUT_SECTION_URL_ROUTE,
        RetrieveApAboutSectionAPIView.as_view()
    )
]
