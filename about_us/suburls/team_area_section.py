from about_us.views.team_area_section import RetrieveTeamAreaSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

TEAM_AREA_SECTION_ROOT_ROUTE = 'retrieve/section/team-area/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_TEAM_AREA_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_TEAM_AREA_SECTION_URL_ROUTE,
         RetrieveTeamAreaSectionAPIView.as_view()),
]
