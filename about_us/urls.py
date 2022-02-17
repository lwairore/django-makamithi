from about_us.suburls.client_review import (
    CLIENT_REVIEW_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as CLIENT_REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION)
from about_us.suburls.client_review_section import (
    CLIENT_REVIEW_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as CLIENT_REVIEW_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from about_us.suburls.team_area_section import (
    TEAM_AREA_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as TEAM_AREA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from about_us.suburls.what_we_do_section import (WHAT_WE_DO_SECTION_ROOT_ROUTE,
                                                 URL_FILE_NAME_WITHOUT_EXTENSION as WHAT_WE_DO_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from about_us.suburls.faq import (
    FAQ_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as FAQ_URL_FILE_NAME_WITHOUT_EXTENSION)
from about_us.suburls.faq_section import (FAQ_SECTION_ROOT_ROUTE,
                                          URL_FILE_NAME_WITHOUT_EXTENSION as FAQ_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from about_us.suburls.seo import (
    ABOUT_US_SEO_DETAILS_ROOT_ROUTE,
    URL_FILE_NAME_WITHOUT_EXTENSION as ABOUT_US_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)
from about_us.suburls.ap_about_section import (AP_ABOUT_SECTION_ROOT_ROUTE,
                                               URL_FILE_NAME_WITHOUT_EXTENSION as AP_ABOUT_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls.conf import include, path
from about_us.suburls import URL_FILE_NAME
from about_us.apps import AboutUsConfig


app_name = AboutUsConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for section Ap About
    path(AP_ABOUT_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+AP_ABOUT_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section About SEO
    path(ABOUT_US_SEO_DETAILS_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+ABOUT_US_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section FAQ
    path(FAQ_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+FAQ_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for FAQ
    path(FAQ_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+FAQ_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for What we do section
    path(WHAT_WE_DO_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+WHAT_WE_DO_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Team area section
    path(TEAM_AREA_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+TEAM_AREA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Client review section
    path(CLIENT_REVIEW_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+CLIENT_REVIEW_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Client review
    path(CLIENT_REVIEW_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+CLIENT_REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
