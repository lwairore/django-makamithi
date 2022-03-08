from footer.views.footer_section import RetrieveFooterSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

FOOTER_SECTION_ROOT_ROUTE = ''

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)


_RETRIEVE_FOOTER_SECTION_URL_ROUTE = 'retrieve/section/footer/'

urlpatterns = [
    #  'URLConf' for 'Footer section'
    path(_RETRIEVE_FOOTER_SECTION_URL_ROUTE,
         RetrieveFooterSectionAPIView.as_view()),
]
