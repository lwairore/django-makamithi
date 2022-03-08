from terms_and_privacy_policy.suburls import URL_FILE_NAME
from terms_and_privacy_policy.apps import TermsAndPrivacyPolicyConfig


app_name = TermsAndPrivacyPolicyConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = []
