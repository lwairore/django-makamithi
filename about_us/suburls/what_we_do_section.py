from about_us.views.what_we_do_section import RetrieveWhatWeDoSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

WHAT_WE_DO_SECTION_ROOT_ROUTE = 'retrieve/section/what-we-do/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_WHAT_WE_DO_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_WHAT_WE_DO_SECTION_URL_ROUTE,
         RetrieveWhatWeDoSectionAPIView.as_view()),
]
