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
from home_two.apps import HomeTwoConfig
from django.conf.urls import include
from django.contrib import admin
from django.urls import path


# default: "Django Administration"
admin.site.site_header = 'Makamithi Administration'

# default: "Site administration"
admin.site.index_title = 'Makamithi Site administration'

admin.site.site_title = 'Makamithi  site admin'  # default: "Django site admin"

# By default , "VIEW SITE" points to '/' i.e localhost:8000
admin.site.site_url = "https://makamithi.com/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banner-ad/', include(
        f'{HomeTwoConfig.name}.urls')),
    # path('products/', include('product.urls')),
]
