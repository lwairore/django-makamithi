import django
from team.models import TeamModel
from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html


@register(TeamModel)
class TeamModelAdmin(ModelAdmin):
    list_display = ('full_name', 'role', 'facebook_social', 'twitter_social',
                    'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)
    search_fields = ('full_name', 'role', 'facebook', 'twitter',)

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
