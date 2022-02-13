from home_two.suburls.gallery_section import (GALLERY_SECTION_ROOT_ROUTE,
                                              URL_FILE_NAME_WITHOUT_EXTENSION as GALLERY_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from home_two.suburls.core_value import (CORE_VALUE_ROOT_ROUTE,
                                         URL_FILE_NAME_WITHOUT_EXTENSION as CORE_VALUE_URL_FILE_NAME_WITHOUT_EXTENSION)
from home_two.suburls.seo import (HOME_SEO_DETAILS_ROOT_ROUTE,
                                  URL_FILE_NAME_WITHOUT_EXTENSION as HOME_SEO_DETAILS_URL_FILE_NAME_WITHOUT_EXTENSION)
from home_two.suburls.why_choose_us_section import (
    WHY_CHOOSE_US_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as WHY_CHOOSE_US_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from home_two.suburls.visit_now_cta_section import (
    VISIT_NOW_CTA_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as VISIT_NOW_CTA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from home_two.suburls.our_feature_section import (
    FEATURE_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as FEATURE_FILE_NAME_WITHOUT_EXTENSION)
from home_two.suburls.about_section import (
    ABOUT_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as ABOUT_SECTION_FILE_NAME_WITHOUT_EXTENSION)
from home_two.suburls.banner_ad import (
    BANNER_AD_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as BANNER_AD_FILE_NAME_WITHOUT_EXTENSION)
from home_two.apps import HomeTwoConfig
from home_two.suburls import URL_FILE_NAME
from django.urls.conf import path, include

app_name = HomeTwoConfig.name


_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for Banner-ads
    path(BANNER_AD_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + BANNER_AD_FILE_NAME_WITHOUT_EXTENSION)),

    #  Routes for About section
    path(ABOUT_SECTION_ROOT_ROUTE,
         include(_BASE_INCLUDE_PATH + ABOUT_SECTION_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Feature section
    path(FEATURE_SECTION_ROOT_ROUTE,
         include(_BASE_INCLUDE_PATH + FEATURE_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Visit now cta section
    path(VISIT_NOW_CTA_SECTION_ROOT_ROUTE,
         include(_BASE_INCLUDE_PATH + VISIT_NOW_CTA_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Why choose us section
    path(WHY_CHOOSE_US_SECTION_ROOT_ROUTE,
         include(_BASE_INCLUDE_PATH + WHY_CHOOSE_US_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Home SEO Details
    path(HOME_SEO_DETAILS_ROOT_ROUTE,
         include(_BASE_INCLUDE_PATH + HOME_SEO_DETAILS_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Core value
    path(CORE_VALUE_ROOT_ROUTE,
         include(_BASE_INCLUDE_PATH + CORE_VALUE_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for Gallery section
    path(GALLERY_SECTION_ROOT_ROUTE,
         include(_BASE_INCLUDE_PATH + GALLERY_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
