from home_two.submodels.preview_item import PhotoModel
from site_breadcrumb.models import SiteBreadcrumbModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveSiteBreadcrumbModelSerializer(ModelSerializer):
    image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = SiteBreadcrumbModel
        fields = ('image', 'id',)
