from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, DecimalField, TextField
from django.db.models.fields.related import ForeignKey, OneToOneField


class TypeOfPlanModel(Model):
    title = CharField(max_length=70)
    description = TextField(max_length=150, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Type of plan'
        verbose_name_plural = 'Types of plan'


class PlanModel(Model):
    price = DecimalField(max_digits=10,
                         decimal_places=2)
    title = CharField(max_length=90)
    description = TextField(max_length=255, blank=True, null=True)
    type_of_plan = ForeignKey(
        'TypeOfPlanModel', blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Service plan'
        verbose_name_plural = 'Service plans'
