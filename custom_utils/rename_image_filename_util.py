from django.utils import timezone
import os
from uuid import uuid4
from django.contrib.contenttypes.models import ContentType
import secrets


def rename_uploaded_image_and_path(instance, filename):
    obj_content_type = ContentType.objects.get_for_model(instance)

    upload_to = '{app}_{model}/{pk}/'.format(
        app=obj_content_type.app_label,
        model=obj_content_type.model,
        pk=obj_content_type.pk,
    )
    ext = filename.split('.')[-1]
    today = timezone.now()
    # this will create something like "2011/08/30"
    today_path = today.strftime("%Y/%m/%d")
    # get filename
    token_urlsafe_prefix = secrets.token_urlsafe(32)

    if instance.pk:
        filename = '{}{}.{}'.format(token_urlsafe_prefix, instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}{}.{}'.format(token_urlsafe_prefix, uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, today_path, filename)
