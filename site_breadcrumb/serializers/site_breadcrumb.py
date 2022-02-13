from home_two.submodels.preview_item import PhotoModel
from site_breadcrumb.models import SiteBreadcrumbModel
from rest_framework.serializers import ModelSerializer


class ListSiteBreadcrumbModelSerializer(ModelSerializer):
    class Meta:
        model = SiteBreadcrumbModel
        fields = ('image', 'id',)
