from service.views.service import ListServiceAPIView
from django.urls.conf import path
from custom_utils.get_file_name_util import get_file_name


URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_SERVICE_ROUTE = ''

LIST_SERVICE_ROOT_ROUTE = 'list/'

urlpatterns = [
    path(_LIST_SERVICE_ROUTE, ListServiceAPIView.as_view()),
]