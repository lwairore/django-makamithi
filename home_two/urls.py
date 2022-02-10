from home_two.suburls.banner_ad import BANNER_AD_URL_FILE_NAME_WITHOUT_EXTENSION
from home_two.apps import HomeTwoConfig
from home_two.suburls import URL_FILE_NAME
from django.urls.conf import path, include

app_name = HomeTwoConfig.name

urlpatterns = [
    path('list/banner-ad/',
         include(f'{app_name}.{URL_FILE_NAME}.{BANNER_AD_URL_FILE_NAME_WITHOUT_EXTENSION}')),
]
