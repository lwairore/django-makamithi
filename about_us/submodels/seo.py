from django.core.exceptions import ValidationError
from social_sharing.submodels.seo_social_share_data import SeoSocialShareDataModel


class AboutUsSEODetailsModel(SeoSocialShareDataModel):
    def clean(self):
        if AboutUsSEODetailsModel.objects.exists() and not self.pk:
            raise ValidationError(
                "You can only have one SEO Configuration for 'Home'")

    def save(self, *args, **kwargs):
        if not self.pk and AboutUsSEODetailsModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "AboutUsSEODetailsModel" instance')
        return super(AboutUsSEODetailsModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Home SEO Detail'
        verbose_name_plural = 'Home SEO Details'
