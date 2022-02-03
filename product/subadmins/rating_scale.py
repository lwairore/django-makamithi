from product.submodels.rating_scale import RatingScaleModel
from django.contrib.admin import ModelAdmin, register


@register(RatingScaleModel)
class RatingScaleModelAdmin(ModelAdmin):
    list_display = ('number_of_five_star',
                    'number_of_four_star', 'number_of_three_star',
                    'number_of_two_star',
                    'number_of_one_star',)
    search_fields = ('review',)

    def number_of_five_star(self, obj):
        five_star_count = obj.five_star.all().count()

        return five_star_count

    number_of_five_star.short_description = 'Five star'

    def number_of_four_star(self, obj):
        four_star_count = obj.four_star.all().count()

        return four_star_count

    number_of_four_star.short_description = 'Four star'

    def number_of_three_star(self, obj):
        three_star_count = obj.three_star.all().count()

        return three_star_count

    number_of_three_star.short_description = 'Three star'

    def number_of_two_star(self, obj):
        two_star_count = obj.two_star.all().count()

        return two_star_count

    number_of_two_star.short_description = 'Two star'

    def number_of_one_star(self, obj):
        one_star_count = obj.one_star.all().count()

        return one_star_count

    number_of_one_star.short_description = 'One star'
