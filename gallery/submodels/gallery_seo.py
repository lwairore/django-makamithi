from django.core.exceptions import ValidationError
from social_sharing.submodels.seo_social_share_data import SeoSocialShareDataModel


class GallerySEODetailsModel(SeoSocialShareDataModel):
    def clean(self):
        if GallerySEODetailsModel.objects.exists() and not self.pk:
            raise ValidationError(
                "You can only have one SEO Configuration for 'Gallery page'")

    def save(self, *args, **kwargs):
        if not self.pk and GallerySEODetailsModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "GallerySEODetailsModel" instance')
        return super(GallerySEODetailsModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Gallery SEO Detail'
        verbose_name_plural = 'Gallery SEO Details'
