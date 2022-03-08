from service.views.service import (ListServiceForAboutPageAPIView, ListServiceForHomePageAPIView,
                                   ListServiceForServicePageAPIView, ListServiceForSidebarSectionAPIView, RetrieveServiceDetailAPIView)
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_SERVICE_FOR_HOME_PAGE_ROUTE = 'home/'

_RETRIEVE_SERVICE_DETAIL_ROUTE = '<int:service_id>/service-details/'

_LIST_SERVICE_FOR_ABOUT_PAGE_ROUTE = 'about/'

_LIST_SERVICE_FOR_SERVICE_PAGE_ROUTE = 'service-area/'

_LIST_SERVICE_FOR_SIDEBAR_SECTION_ROUTE = 'service-area/sidebar/'

LIST_SERVICE_ROOT_ROUTE = 'list/'

urlpatterns = [
    # Service for home page section
    path(_LIST_SERVICE_FOR_HOME_PAGE_ROUTE,
         ListServiceForHomePageAPIView.as_view()),

    # Service for about page section
    path(_LIST_SERVICE_FOR_ABOUT_PAGE_ROUTE,
         ListServiceForAboutPageAPIView.as_view()),

    # Service for service page
    path(_LIST_SERVICE_FOR_SERVICE_PAGE_ROUTE,
         ListServiceForServicePageAPIView.as_view()),

    # Service for service sidebar section
    path(_LIST_SERVICE_FOR_SIDEBAR_SECTION_ROUTE,
         ListServiceForSidebarSectionAPIView.as_view()),

    # Service for service detail
    path(_RETRIEVE_SERVICE_DETAIL_ROUTE,
         RetrieveServiceDetailAPIView.as_view()),
]
