from team.models import TeamModel
from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _TeamModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_TeamModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

    class Meta:
        model = TeamModel
        fields = '__all__'


@register(TeamModel)
class TeamModelAdmin(ModelAdmin):
    form = _TeamModelForm
    list_display = ('full_name', 'role', 'facebook_social', 'twitter_social',
                    'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)
    readonly_fields = ('modified_date', 'created_at', 'image_preview',)
    search_fields = ('full_name', 'role', 'facebook', 'twitter',)
    fieldsets = (
        (None, {
            'fields': ('full_name', 'role',),
        }),
        ('Preview', {
            'fields': ('image', 'image_preview',
                       ),
        }),
        ('Social media', {
            'fields': ('facebook', 'twitter',
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

    def facebook_social(self, obj: TeamModel):
        facebook = obj.facebook

        if facebook:
            return format_html(f"<a href='{facebook}' target='_blank'>{facebook}</a>")
        return '-'

    facebook_social.short_description = 'Facebook Social'

    def twitter_social(self, obj: TeamModel):
        twitter = obj.twitter

        if twitter:
            return format_html(f"<a href='{twitter}' target='_blank'>{twitter}</a>")
        return '-'

    twitter_social.short_description = 'Twitter Social'
