from product.suburls.reviews import REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION
from home.apps import HomeConfig
from home.urls import URL_FILE_NAME
from django.urls.conf import path, include

app_name = HomeConfig.name

urlpatterns = [
    path('banner',
         include(f'{app_name}.{URL_FILE_NAME}.{REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION}')),
]
