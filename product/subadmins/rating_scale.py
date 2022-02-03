from product.submodels.rating_scale import RatingScaleModel
from django.contrib.admin import ModelAdmin, register


@register(RatingScaleModel)
class RatingScaleModelAdmin(ModelAdmin):
    list_display = ('number_of_five_star',)
    search_fields = ('review',)

    def number_of_five_star(self, obj):
        five_star_count = obj.five_star.all().count()

        return five_star_count

    number_of_five_star.short_description = 'Five star'
