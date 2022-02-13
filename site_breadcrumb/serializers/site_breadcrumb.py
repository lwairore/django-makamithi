from home_two.submodels.preview_item import PhotoModel
from site_breadcrumb.models import SiteBreadcrumbModel
from rest_framework.serializers import ModelSerializer


class ListSiteBreadcrumbModelSerializer(ModelSerializer):
    image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = SiteBreadcrumbModel
        fields = ('image', 'id',)
