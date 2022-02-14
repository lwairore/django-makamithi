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
             _BASE_INCLUDE_PATH+ABOUT_US_SEO_URL_FILE_NAME_WITHOUT_EXTENSION))
]
