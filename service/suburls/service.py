from service.views.service import ListServiceForAboutPageAPIView, ListServiceForHomePageAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_SERVICE_FOR_HOME_PAGE_ROUTE = 'home/'

_LIST_SERVICE_FOR_ABOUT_PAGE_ROUTE = 'about/'

_LIST_SERVICE_FOR_SERVICE_PAGE_ROUTE = 'service-area/'

LIST_SERVICE_ROOT_ROUTE = 'list/'

urlpatterns = [
    path(_LIST_SERVICE_FOR_HOME_PAGE_ROUTE,
         ListServiceForHomePageAPIView.as_view()),
    path(_LIST_SERVICE_FOR_ABOUT_PAGE_ROUTE,
         ListServiceForAboutPageAPIView.as_view()),
    path(_LIST_SERVICE_FOR_SERVICE_PAGE_ROUTE,
         ListServiceForAboutPageAPIView.as_view()),
]
