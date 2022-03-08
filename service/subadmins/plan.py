from service.submodels.plan import BenefitModel, PlanModel, TypeOfPlanModel
from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html


@register(BenefitModel)
class BenefitModelAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'modified_date',)
    search_fields = ('title', 'description',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'modified_date',)


@register(TypeOfPlanModel)
class TypeOfPlanModelAdmin(ModelAdmin):
    list_display = ('title', 'image',)
    search_fields = ('title', 'description',)
    raw_id_fields = ('image',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)


@register(PlanModel)
class PlanModelAdmin(ModelAdmin):
    list_display = ('price', 'selected_plan', 'selected_benefits',)
    search_fields = ('price', )
    filter_horizontal = ('benefits',)
    raw_id_fields = ('type_of_plan',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)

    def selected_plan(self, obj: PlanModel):
        plan_title = 'Not selected'

        try:
            plan_title = obj.type_of_plan.title
        except AttributeError:
            pass

        return format_html("<b><i>{}</i></b>", plan_title)

    selected_plan.short_description = 'Selected plan'

    def selected_benefits(self, obj: PlanModel):
        benefit_count = obj.benefits.all()\
            .order_by().only('id').count()

        return format_html("<b><i>{}</i></b>", benefit_count)

    selected_benefits.short_description = 'Selected benefits'
