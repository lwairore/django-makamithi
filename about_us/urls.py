from about_us.suburls import URL_FILE_NAME
from about_us.apps import AboutUsConfig


app_name = AboutUsConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)
    
urlpatterns = []
