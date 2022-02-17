from contact_us.suburls import URL_FILE_NAME
from contact_us.apps import ContactUsConfig

app_name = ContactUsConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = []
