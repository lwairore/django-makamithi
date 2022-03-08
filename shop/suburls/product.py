from shop.views.product_review import ListProductReviewAPIView
from shop.views.product import (ListProductForHomePageAPIView,
                                ListProductForShopPageAPIView, RetrieveProductDetailAPIView)
from django.urls import path
from shop.suburls.product_category import PRODUCT_CATEGORY_ROOT_ROUTE
from custom_utils.get_file_name_util import get_file_name


URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

PRODUCT_CATEGORY_ROUTE_PARAMETER = '<int:product_category_id>'

_PRODUCT_ID_ROUTE_PARAMETER = '<int:product_id>'

PRODUCT_ROOT_ROUTE = 'list/products/'

_LIST_PRODUCT_FOR_HOME_PAGE_ROUTE = PRODUCT_CATEGORY_ROOT_ROUTE + \
    PRODUCT_CATEGORY_ROUTE_PARAMETER + '/'

_LIST_PRODUCT_FOR_SHOP_PAGE_ROUTE = ''

_RETRIEVE_PRODUCT_DETAIL_ROUTE = f'{_PRODUCT_ID_ROUTE_PARAMETER}/details/'

_LIST_PRODUCT_REVIEW_ROUTE = f'{_RETRIEVE_PRODUCT_DETAIL_ROUTE}reviews/'

urlpatterns = [
    # List of products for a given category
    path(_LIST_PRODUCT_FOR_HOME_PAGE_ROUTE,
         ListProductForHomePageAPIView.as_view()),

    # List of products for shop section
    path(_LIST_PRODUCT_FOR_SHOP_PAGE_ROUTE,
         ListProductForShopPageAPIView.as_view()),

    # Retrieve product details
    path(_RETRIEVE_PRODUCT_DETAIL_ROUTE,
         RetrieveProductDetailAPIView.as_view()),

    # List product reviews
    path(_LIST_PRODUCT_REVIEW_ROUTE,
         ListProductReviewAPIView.as_view(),)
]
