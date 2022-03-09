from service.submodels.plan import BenefitModel, PlanModel, TypeOfPlanModel
from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _BenefitModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_BenefitModelForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True

    class Meta:
        model = BenefitModel
        fields = '__all__'


@register(BenefitModel)
class BenefitModelAdmin(ModelAdmin):
    form = _BenefitModelForm
    list_display = ('title', 'created_at', 'modified_date',)
    search_fields = ('title', 'description',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date',)


class _TypeOfPlanModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_TypeOfPlanModelForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True
        self.fields['image'].required = True

    class Meta:
        model = TypeOfPlanModel
        fields = '__all__'


@register(TypeOfPlanModel)
class TypeOfPlanModelAdmin(ModelAdmin):
    form = _TypeOfPlanModelForm
    list_display = ('title', 'image',)
    search_fields = ('title', 'description',)
    raw_id_fields = ('image',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date', 'image_preview',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description',),
        }),
        ('Image', {
            'fields': ('image', 'image_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.image.image.url,
        ))


class _PlanModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_PlanModelForm, self).__init__(*args, **kwargs)
        self.fields['type_of_plan'].required = True
        self.fields['benefits'].required = True

    class Meta:
        model = PlanModel
        fields = '__all__'


@register(PlanModel)
class PlanModelAdmin(ModelAdmin):
    form = _PlanModelForm
    list_display = ('price', 'selected_plan', 'selected_benefits',)
    search_fields = ('price', )
    filter_horizontal = ('benefits',)
    raw_id_fields = ('type_of_plan',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date',)

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
