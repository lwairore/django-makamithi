from home_two.views.about_section import RetrieveAboutSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_ABOUT_SECTION_ROUTE = ''

ABOUT_SECTION_ROOT_ROUTE = 'retrieve/about-section'

urlpatterns = [
    path(_RETRIEVE_ABOUT_SECTION_ROUTE, RetrieveAboutSectionAPIView.as_view()),
]
