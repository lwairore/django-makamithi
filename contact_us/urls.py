from contact_us.suburls.seo import (CONTACT_US_SEO_DETAILS_ROOT_ROUTE,
                                    URL_FILE_NAME_WITHOUT_EXTENSION as CONTACT_US_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)
from contact_us.suburls.contact_info import (CONTACT_INFO_ROOT_ROUTE,
                                             URL_FILE_NAME_WITHOUT_EXTENSION as CONTACT_INFO_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls import path, include
from contact_us.suburls import URL_FILE_NAME
from contact_us.apps import ContactUsConfig

app_name = ContactUsConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for section contact info
    path(CONTACT_INFO_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+CONTACT_INFO_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section About SEO
    path(CONTACT_US_SEO_DETAILS_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+CONTACT_US_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
