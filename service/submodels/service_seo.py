from django.core.exceptions import ValidationError
from social_sharing.submodels.seo_social_share_data import SeoSocialShareDataModel


class ServiceSEODetailsModel(SeoSocialShareDataModel):
    def clean(self):
        if ServiceSEODetailsModel.objects.exists() and not self.pk:
            raise ValidationError(
                "You can only have one SEO Configuration for 'Service page'")

    def save(self, *args, **kwargs):
        if not self.pk and ServiceSEODetailsModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "ServiceSEODetailsModel" instance')
        return super(ServiceSEODetailsModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Service SEO Detail'
        verbose_name_plural = 'Service SEO Details'
