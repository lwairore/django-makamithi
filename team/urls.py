from team.suburls.seo import (
    TEAM_SEO_DETAILS_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as TEAM_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)
from team.suburls.team import (
    TEAM_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as TEAM_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls import path, include
from team.suburls import URL_FILE_NAME
from team.apps import TeamConfig

app_name = TeamConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for Team
    path(
        TEAM_ROOT_ROUTE,
        include(
            _BASE_INCLUDE_PATH + TEAM_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Team SEO
    path(TEAM_SEO_DETAILS_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+TEAM_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
