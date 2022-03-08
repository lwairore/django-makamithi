from django.urls import path
from team.views.seo import RetrieveTeamSEODetailsAPIView
from custom_utils.get_file_name_util import get_file_name


TEAM_SEO_DETAILS_ROOT_ROUTE = 'retrieve/seo/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_TEAM_SEO_DETAILS_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_TEAM_SEO_DETAILS_URL_ROUTE,
        RetrieveTeamSEODetailsAPIView.as_view()
    ),
]
