from home_two.submodels.preview_item import PhotoModel
from django.db.models import (
    Model, ForeignKey, CharField, PROTECT)
from django.db.models.fields import DateTimeField, TextField


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


class ProductReview(Model):
    full_name = CharField(max_length=70)
    client_image = ForeignKey(PhotoModel, blank=True,
                              null=True, on_delete=PROTECT)
    review = TextField(max_length=5000)
    rating = CharField(
        max_length=11,
        choices=FIVE_POINT_NUMERICAL_RATING_SCALE,
        default=FIVE_POINTS_SCALE, )
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product reviews'
