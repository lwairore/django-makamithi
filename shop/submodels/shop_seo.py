from django.core.exceptions import ValidationError
from social_sharing.submodels.seo_social_share_data import SeoSocialShareDataModel


class ShopSEODetailsModel(SeoSocialShareDataModel):
    def clean(self):
        if ShopSEODetailsModel.objects.exists() and not self.pk:
            raise ValidationError(
                "You can only have one SEO Configuration for 'Shop page'")

    def save(self, *args, **kwargs):
        if not self.pk and ShopSEODetailsModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "ShopSEODetailsModel" instance')
        return super(ShopSEODetailsModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Shop SEO Detail'
        verbose_name_plural = 'Shop SEO Details'
