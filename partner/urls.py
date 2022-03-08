from partner.suburls.partner import (
    PARTNER_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as PARTNER_URL_FILE_NAME_WITHOUT_EXTENSION)
from partner.suburls.partner_area_section import (
    PARTNER_AREA_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as PARTNER_AREA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls import path, include
from partner.apps import PartnerConfig
from partner.suburls import URL_FILE_NAME


app_name = PartnerConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for section Partner Area
    path(PARTNER_AREA_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+PARTNER_AREA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for PARTNER
    path(PARTNER_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+PARTNER_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
