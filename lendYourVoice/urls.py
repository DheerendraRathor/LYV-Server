"""lendYourVoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import re

import rest_framework_swagger.urls
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.views.static import serve

from lyv.views import BookViewSet, ParagraphViewSet, RecordingViewSet
from account.views import AccountViewSet

router = DefaultRouter()
router.register('book', BookViewSet, base_name='book')
router.register('paragraph', ParagraphViewSet, base_name='paragraph')
router.register('recording', RecordingViewSet, base_name='recording')
router.register('account', AccountViewSet, base_name='account')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-docs/', include(rest_framework_swagger.urls, namespace='api-docs')),
]

urlpatterns += [
    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve,
        kwargs={
            'document_root': settings.STATIC_ROOT,
        }
        ),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve,
        kwargs={
            'document_root': settings.MEDIA_ROOT,
        }
        ),
]
