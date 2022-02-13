from home_two.views.core_value import ListCoreValueAPIView
from django.urls.conf import path
from custom_utils.get_file_name_util import get_file_name


CORE_VALUE_ROOT_ROUTE = 'list/core-value/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_CORE_VALUE_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_CORE_VALUE_URL_ROUTE,
         ListCoreValueAPIView.as_view()),
]
