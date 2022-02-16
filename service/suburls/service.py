from service.views.service import ListAboutServiceAPIView, ListHomeServiceAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_HOME_SERVICE_ROUTE = 'home/'

_LIST_ABOUT_SERVICE_ROUTE = 'about/'

LIST_SERVICE_ROOT_ROUTE = 'list/'

urlpatterns = [
    path(_LIST_HOME_SERVICE_ROUTE, ListHomeServiceAPIView.as_view()),
    path(_LIST_ABOUT_SERVICE_ROUTE, ListAboutServiceAPIView.as_view()),
]
