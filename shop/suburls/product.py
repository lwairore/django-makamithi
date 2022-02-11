from shop.suburls.product_category import PRODUCT_CATEGORY_ROOT_ROUTE
from custom_utils.get_file_name_util import get_file_name


URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_PRODUCT_ROUTE = 'list/'

PRODUCT_CATEGORY_ROUTE_PARAMETER = '<int:product_category_id>'

PRODUCT_ROOT_ROUTE = PRODUCT_CATEGORY_ROOT_ROUTE + \
    PRODUCT_CATEGORY_ROUTE_PARAMETER+'/products/'
