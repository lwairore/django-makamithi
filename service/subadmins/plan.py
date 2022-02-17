from service.submodels.plan import PlanModel, TypeOfPlanModel
from django.contrib.admin import ModelAdmin, register


@register(TypeOfPlanModel)
class TypeOfPlanModelAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)


@register(PlanModel)
class PlanModelAdmin(ModelAdmin):
    list_display = ('title', 'price',)
    search_fields = ('title', 'description', 'price',)
    raw_id_fields = ('type_of_plan',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)
