from django.core.exceptions import ValidationError
from social_sharing.submodels.seo_social_share_data import SeoSocialShareDataModel


class ContactUsSEODetailsModel(SeoSocialShareDataModel):
    def clean(self):
        if ContactUsSEODetailsModel.objects.exists() and not self.pk:
            raise ValidationError(
                "You can only have one SEO Configuration for 'Contact us page'")

    def save(self, *args, **kwargs):
        if not self.pk and ContactUsSEODetailsModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "ContactUsSEODetailsModel" instance')
        return super(ContactUsSEODetailsModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Contact Us SEO Detail'
        verbose_name_plural = 'Contact Us SEO Details'
