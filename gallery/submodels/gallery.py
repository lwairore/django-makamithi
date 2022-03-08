from shop.submodels.product_category import ProductCategoryModel
from django.db.models.fields import DateTimeField
from home_two.submodels import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import CharField, TextField


class GalleryModel(Model):
    title = CharField(max_length=70, blank=True, null=True)
    keywords = CharField(max_length=180, blank=True, null=True)
    gallery_preview = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT,
        related_name='gallery_gallery_preview')
    home_preview = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT,
        related_name='gallery_home_preview')
    layout_image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT,
        related_name='gallery_layout_image')
    category = ForeignKey(ProductCategoryModel,
                          blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)
    occured_on = DateTimeField(blank=True, null=True)
    description = TextField(max_length=5000, blank=True, null=True)

    def __str__(self) -> str:
        return f'Gallery ID={self.id}'

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
