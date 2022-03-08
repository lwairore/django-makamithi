from django.db.models import Model
from django.db.models.fields import (
    BooleanField,
    CharField, EmailField, TextField, DateTimeField)


class InboxModel(Model):
    name = CharField(max_length=180)
    email = EmailField(blank=True, null=True)
    phone_number = CharField(max_length=17)
    subject = CharField(max_length=250, blank=True, null=True)
    message = TextField(max_length=5000, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)
    read = BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Inbox'
        verbose_name_plural = 'Inbox'
