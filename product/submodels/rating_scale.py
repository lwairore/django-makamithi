from django.db.models import Model
from django.db.models.fields import CharField, TextField

FIVE_POINTS_SCALE = '5'
FOUR_POINTS_SCALE = '4'
THREE_POINTS_SCALE = '3'
TWO_POINTS_SCALE = '2'
ONE_POINT_SCALE = '1'

FIVE_POINT_NUMERICAL_RATING_SCALE = (
    (FIVE_POINTS_SCALE, 'Five stars'),
    (FOUR_POINTS_SCALE, 'Four stars'),
    (THREE_POINTS_SCALE, 'Three stars'),
    (TWO_POINTS_SCALE, 'Two stars'),
    (ONE_POINT_SCALE, 'One star'),
)


class ProductReviewModel(Model):
    rating = CharField(
        max_length=11,
        choices=FIVE_POINT_NUMERICAL_RATING_SCALE,
        default=FIVE_POINTS_SCALE,
    )

    review = TextField(max_length=5000)

    def __str__(self) -> str:
        return self.rating

    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product reviews'
