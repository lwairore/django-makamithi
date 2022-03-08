from django.urls import path, include
from social_media.suburls.social_media import (
    SOCIAL_MEDIA_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as SOCIAL_MEDIA_URL_FILE_NAME_WITHOUT_EXTENSION)
from social_media.suburls import URL_FILE_NAME
from social_media.apps import SocialMediaConfig


app_name = SocialMediaConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for Social media
    path(
        SOCIAL_MEDIA_ROOT_ROUTE,
        include(
            _BASE_INCLUDE_PATH + SOCIAL_MEDIA_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
