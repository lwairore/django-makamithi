from django.db.models.fields import DateTimeField
from django.db.models import Model
from django.db.models.fields import CharField, URLField


class SocialMediaModel(Model):
    title = CharField(max_length=70)
    icon = CharField(max_length=70, blank=True, null=True)
    link = URLField(max_length=180)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Social media'
        verbose_name_plural = 'Social medias'
