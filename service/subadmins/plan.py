from service.submodels.plan import TypeOfPlanModel
from django.contrib.admin import ModelAdmin, register


@register(TypeOfPlanModel)
class TypeOfPlanModelAdmin(ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)
    raw_id_fields = ('description',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)
