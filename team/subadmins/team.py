from team.models import TeamModel
from django.contrib.admin import ModelAdmin, register


@register(TeamModel)
class TeamModelAdmin(ModelAdmin):
    list_display = ('full_name', 'role', 'facebook', 'twitter',
                    'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)
    search_fields = ('full_name', 'role', 'facebook', 'twitter',)
