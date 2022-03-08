from contact_us.suburls.contact_info import (
    CONTACT_INFO_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as CONTACT_INFO_URL_FILE_NAME_WITHOUT_EXTENSION)
from footer.suburls.footer_section import (
    FOOTER_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as FOOTER_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls import path, include
from footer.suburls import URL_FILE_NAME
from footer.apps import FooterConfig


app_name = FooterConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)


urlpatterns = [
    # Routes for `sub app` 'footer section'
    path(FOOTER_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + FOOTER_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION
         )),

    # Routes for `sub app` 'contact info section'
    path(CONTACT_INFO_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + CONTACT_INFO_URL_FILE_NAME_WITHOUT_EXTENSION
         )),
]
