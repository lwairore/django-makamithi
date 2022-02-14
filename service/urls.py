from service.suburls import URL_FILE_NAME
from service.suburls.service import LIST_SERVICE_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION
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
             _BASE_INCLUDE_PATH + URL_FILE_NAME_WITHOUT_EXTENSION
         ))
]
