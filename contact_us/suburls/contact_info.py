from contact_us.views.contact_info import ListContactInfoAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


CONTACT_INFO_ROOT_ROUTE = 'list/contact-info/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_CONTACT_INFO_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_CONTACT_INFO_URL_ROUTE,
         ListContactInfoAPIView.as_view()),
]