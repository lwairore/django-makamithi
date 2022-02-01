from product.submodels.product import ProductModel
from product.submodels.category import ProductCategoryModel
from django.contrib.admin import ModelAdmin, register
from django.db.models import Count


@register(ProductCategoryModel)
class ProductCategoryModelAdmin(ModelAdmin):
    list_display = ('title', 'number_of_products',)
    search_fields = ('title', 'description',)

    def number_of_products(self, obj):
        products_count = obj.product_category.all()\
            .order_by().only('id').count()

        return products_count
