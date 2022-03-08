from django.core.exceptions import ValidationError
from social_sharing.submodels.seo_social_share_data import SeoSocialShareDataModel


class TeamSEODetailsModel(SeoSocialShareDataModel):
    def clean(self):
        if TeamSEODetailsModel.objects.exists() and not self.pk:
            raise ValidationError(
                "You can only have one SEO Configuration for 'About us page'")

    def save(self, *args, **kwargs):
        if not self.pk and TeamSEODetailsModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "TeamSEODetailsModel" instance')
        return super(TeamSEODetailsModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Team SEO Detail'
        verbose_name_plural = 'Team SEO Details'
