from team.views.team import ListTeamAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


TEAM_ROOT_ROUTE = 'list/team/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_TEAM_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_TEAM_URL_ROUTE,
         ListTeamAPIView.as_view()),
]
