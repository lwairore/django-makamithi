from django.db.models.fields import (
    CharField, DateTimeField, EmailField, BooleanField)
from django.db.models import Model, Manager


class FooterManager(Manager):
    def get_queryset(self):
        return super(FooterManager,
                     self).get_queryset()\
            .filter(can_appear_on_footer=True)


class ContactInfoModel(Model):
    address_title = CharField(max_length=70)
    address = CharField(max_length=150)
    email = EmailField()
    phone_number = CharField(max_length=15)
    can_appear_on_footer = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)
    objects = Manager()  # The default manager.
    footer = FooterManager()  # Our custom manager.

    def __str__(self) -> str:
        return self.address_title

    class Meta:
        verbose_name = 'Contact info'
        verbose_name_plural = 'Contact infos'
