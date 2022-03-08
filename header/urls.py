from header.suburls.header_section import (
    HEADER_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as HEADER_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from header.suburls.sidebar import (
    SIDEBAR_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as SIDEBAR_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls import path, include
from header.suburls import URL_FILE_NAME
from header.apps import HeaderConfig


app_name = HeaderConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)


urlpatterns = [
    # Routes for `sub app` 'sidebar'
    path(SIDEBAR_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + SIDEBAR_URL_FILE_NAME_WITHOUT_EXTENSION
         )),

    # Routes for `sub app` 'header section'
    path(HEADER_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + HEADER_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION
         )),
]
