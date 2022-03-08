from partner.views.partner import ListPartnerModelAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


PARTNER_ROOT_ROUTE = 'list/partner/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_PARTNER_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_PARTNER_URL_ROUTE,
         ListPartnerModelAPIView.as_view()),
]
