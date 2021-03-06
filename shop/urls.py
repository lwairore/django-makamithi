from shop.suburls.shop_seo import (
    SHOP_SEO_DETAILS_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as SHOP_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)
from shop.suburls.product import (
    PRODUCT_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as PRODUCT_URL_FILE_NAME_WITHOUT_EXTENSION)
from shop.suburls.product_category import (PRODUCT_CATEGORY_ROOT_ROUTE,
                                           URL_FILE_NAME_WITHOUT_EXTENSION as PRODUCT_CATEGORY_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls import path, include
from shop.suburls import URL_FILE_NAME
from shop.apps import ShopConfig


app_name = ShopConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for product category
    path(PRODUCT_CATEGORY_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + PRODUCT_CATEGORY_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for product
    path(PRODUCT_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + PRODUCT_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Shop SEO
    path(SHOP_SEO_DETAILS_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+SHOP_SEO_URL_FILE_NAME_WITHOUT_EXTENSION)),

]
