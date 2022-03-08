"""makamithi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from partner.apps import PartnerConfig
from footer.apps import FooterConfig
from social_media.apps import SocialMediaConfig
from header.apps import HeaderConfig
from terms_and_privacy_policy.apps import TermsAndPrivacyPolicyConfig
from inbox.apps import InboxConfig
from team.apps import TeamConfig
from about_us.apps import AboutUsConfig
from contact_us.apps import ContactUsConfig
from site_breadcrumb.apps import SiteBreadcrumbConfig
from gallery.apps import GalleryConfig
from service.apps import ServiceConfig
from shop.apps import ShopConfig
from home_two.apps import HomeTwoConfig
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# default: "Django Administration"
admin.site.site_header = 'Makamithi Administration'

# default: "Site administration"
admin.site.index_title = 'Makamithi Site administration'

admin.site.site_title = 'Makamithi  site admin'  # default: "Django site admin"

# By default , "VIEW SITE" points to '/' i.e localhost:8000
admin.site.site_url = "https://makamithi.com/"

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLConfs for `home` application
    path('home/', include(
        f'{HomeTwoConfig.name}.urls')),

    # URLConfs for `service` application
    path('service/', include(
        f'{ServiceConfig.name}.urls')),

    # URLConfs for `shop` application
    path('shop/', include(
        f'{ShopConfig.name}.urls')),

    # URLConfs for `gallery` application
    path('gallery/', include(
        f'{GalleryConfig.name}.urls')),

    # URLConfs for `site_breadcrumb` application
    path('site-breadcrumb/', include(
        f'{SiteBreadcrumbConfig.name}.urls')),

    # URLConfs for `about_us` application
    path('about-us/', include(
        f'{AboutUsConfig.name}.urls')),

    # URLConfs for `contact_us` application
    path('contact-us/', include(
        f'{ContactUsConfig.name}.urls')),

    # URLConfs for `team` application
    path('team/', include(
        f'{TeamConfig.name}.urls')),

    # URLConfs for `social_media` application
    path('social-media/', include(
        f'{SocialMediaConfig.name}.urls')),

    # URLConfs for `inbox` application
    path('inbox/', include(
        f'{InboxConfig.name}.urls')),

    # URLConfs for `Terms and privacy policy` application
    # path('terms-and-privacy-policy/', include(
    #     f'{TermsAndPrivacyPolicyConfig.name}.urls')),

    # URLConfs for `header` application
    path('header/', include(
        f'{HeaderConfig.name}.urls')),

    # URLConfs for `footer` application
    path('footer/', include(
        f'{FooterConfig.name}.urls')),

        # URLConfs for `partner` application
    path('partner/', include(
        f'{PartnerConfig.name}.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
