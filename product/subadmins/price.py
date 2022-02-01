from django.contrib.admin.options import ModelAdmin


class PriceModelAdmin(ModelAdmin):
    list_display = ('now', 'was', 'per',)
    fieldsets = (
        (None, {
            'fields': ('now', 'was', 'per',)
        },),
    )
