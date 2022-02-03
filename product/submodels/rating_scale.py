from django.db.models import Model
from django.db.models.fields import TextField
from django.db.models.fields.related import ManyToManyField


class RatingScaleModel(Model):
    review = TextField(max_length=5000)

    def __str__(self) -> str:
        return self.review[:30]

    class Meta:
        verbose_name = 'Rating Scale'
        verbose_name_plural = 'Rating scales'


class FivePointRatingScaleModel(Model):
    five_star = ManyToManyField(
        RatingScaleModel, blank=True, related_name='five_star')
    four_star = ManyToManyField(
        RatingScaleModel, blank=True, related_name='four_star')
    three_star = ManyToManyField(
        RatingScaleModel, blank=True, related_name='three_star')
    two_star = ManyToManyField(
        RatingScaleModel, blank=True, related_name='two_star')
    one_star = ManyToManyField(
        RatingScaleModel, blank=True, related_name='one_star')

    def __str__(self) -> str:
        return f'Rating scale {self.id}'

    class Meta:
        verbose_name = 'Five point rating scale'
        verbose_name_plural = 'Five point rating scales'
