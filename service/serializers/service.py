from rest_framework.fields import DecimalField
from service.submodels.plan import BenefitModel, PlanModel, TypeOfPlanModel
from home_two.submodels.preview_item import PhotoModel
from service.submodels.service import ServiceModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveServiceForHomePageSerializer(ModelSerializer):
    home_photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = ServiceModel
        fields = ('home_photo', 'id', 'title', 'summary')


class RetrieveServiceForAboutPageSerializer(ModelSerializer):
    about_photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = ServiceModel
        fields = ('about_photo', 'id', 'title', 'summary')


class RetrieveServiceForServicePageSerializer(ModelSerializer):
    service_page_photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = ServiceModel
        fields = ('service_page_photo', 'id', 'title', 'summary')


class RetrieveServiceForSidebarSectionSerializer(ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ('id', 'title',)


class _RetrieveTypeOfPlanModelSerializer(ModelSerializer):
    image = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = TypeOfPlanModel
        fields = ('title', 'image',)


class _RetrieveBenefitModelSerializer(ModelSerializer):
    class Meta:
        model = BenefitModel
        fields = ('title', 'description',)


class _PlanModelSerializer(ModelSerializer):
    type_of_plan = _RetrieveTypeOfPlanModelSerializer(required=False)
    benefits = _RetrieveBenefitModelSerializer(many=True, required=False)

    class Meta:
        model = PlanModel
        fields = ('price', 'type_of_plan', 'benefits',)
        extra_kwargs = {
            'price': {
                'required': False
            }
        }


class RetrieveServiceDetalSerializer(ModelSerializer):
    service_detail_photo = _RetrievePhotoModelModelSerializer(required=False)
    plans = _PlanModelSerializer(required=False, many=True)

    class Meta:
        model = ServiceModel
        fields = ('title', 'keywords', 'description', 'service_detail_photo',
                  'plans', 'created_at', 'modified_date',)
