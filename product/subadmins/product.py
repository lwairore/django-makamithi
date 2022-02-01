from django.utils.html import format_html
from product.submodels.product import ProductModel
from django.contrib.admin import ModelAdmin, register
from django.urls import reverse


@register(ProductModel)
class ProductModelAdmin(ModelAdmin):
    list_display = ('title', 'view_category_link',)
    raw_id_fields = ('category',)
    fieldsets = (
        (None, {
            'fields': ('title',)
        },),
        ('Product category', {
            'fields': ('category',)
        },),
        ('Price', {
            'fields': ('price',)
        },),
    )
    search_fields = ('title',)

    def view_category_link(self, obj):
        category_id = obj.category.id
        category_title = obj.category.title

        url = (
            reverse("admin:product_productcategorymodel_change",
                    args=(category_id,))
        )

        return format_html('{} - <a href="{}"> <b><i>View category</i></b> </a>', category_title, url)

    view_category_link.short_description = 'Category'
