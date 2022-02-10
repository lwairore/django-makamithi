# from django.db.models import Model
# from django.db.models.fields import (CharField, DateTimeField, TextField)


# class ProductCategoryModel(Model):
#     title = CharField(max_length=250)
#     description = TextField(max_length=5000, blank=True, null=True)
#     created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
#     modified_date = DateTimeField(auto_now=True, blank=True, null=True)

#     def __str__(self) -> str:
#         return self.title

#     class Meta:
#         verbose_name = 'Product category'
#         verbose_name_plural = 'Product categories'
