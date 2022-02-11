from shop.suburls import URL_FILE_NAME
from shop.apps import ShopConfig


app_name = ShopConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = []
