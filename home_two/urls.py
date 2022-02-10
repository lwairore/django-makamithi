from home_two.suburls.about_section import ABOUT_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as ABOUT_SECTION_FILE_NAME_WITHOUT_EXTENSION
from home_two.suburls.banner_ad import BANNER_AD_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as BANNER_AD_FILE_NAME_WITHOUT_EXTENSION
from home_two.apps import HomeTwoConfig
from home_two.suburls import URL_FILE_NAME
from django.urls.conf import path, include

app_name = HomeTwoConfig.name

urlpatterns = [
    # Routes for Banner-ads
    path(BANNER_AD_ROOT_ROUTE,
         include(f'{app_name}.{URL_FILE_NAME}.{BANNER_AD_FILE_NAME_WITHOUT_EXTENSION}')),

    #  Routes for About section
    path(ABOUT_SECTION_ROOT_ROUTE,
         include(f'{app_name}.{URL_FILE_NAME}.{ABOUT_SECTION_FILE_NAME_WITHOUT_EXTENSION}')),
]
