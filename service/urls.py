from service.suburls.service_sidebar_section import (
    SERVICE_SIDEBAR_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as SERVICE_SIDEBAR_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from service.suburls.about_section import (
    SERVICE_ABOUT_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as SERVICE_ABOUT_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from service.suburls.video import (
    VIDEO_ROOT_ROUTE,
    URL_FILE_NAME_WITHOUT_EXTENSION as VIDEO_URL_FILE_NAME_WITHOUT_EXTENSION)
from service.suburls.service_area_section import (
    SERVICE_AREA_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as SERVICE_AREA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from service.suburls.service_seo import (
    SERVICE_SEO_DETAILS_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as SERVICE_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)
from service.suburls.pricing_area_section import (
    PRICING_AREA_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as PRICING_AREA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from service.suburls import URL_FILE_NAME
from service.suburls.service import (LIST_SERVICE_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as SERVICE_URL_FILE_NAME_WITHOUT_EXTENSION)
from service.apps import ServiceConfig
from django.urls import path, include

app_name = ServiceConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for showing list of services
    path(LIST_SERVICE_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + SERVICE_URL_FILE_NAME_WITHOUT_EXTENSION
         )),

    # Routes for Pricing area section
    path(PRICING_AREA_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+PRICING_AREA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Service SEO
    path(SERVICE_SEO_DETAILS_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+SERVICE_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Service Area
    path(SERVICE_AREA_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+SERVICE_AREA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Service About section
    path(SERVICE_ABOUT_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+SERVICE_ABOUT_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Service Sidebar section
    path(SERVICE_SIDEBAR_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+SERVICE_SIDEBAR_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Video Area
    path(VIDEO_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+VIDEO_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
