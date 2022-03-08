from django.core.exceptions import ValidationError
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models import Model

class PrivacyPolicyModel(Model):
    section_name = CharField(max_length=180)
    content = TextField(max_length=5000)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.section_name

    def clean(self):
        if PrivacyPolicyModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and PrivacyPolicyModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "PrivacyPolicyModel" instance')
        return super(PrivacyPolicyModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Privacy policy'
        verbose_name_plural = 'Privacy policy'
