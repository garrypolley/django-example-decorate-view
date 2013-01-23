from django.conf.urls import patterns, url

from userprofile.views import TestCBVDecorator
from userprofile.views import TestCBVDecorator404

urlpatterns = patterns('',
    # Examples:
    url(r'^cbv/?$', TestCBVDecorator.as_view(), name='cbv'),
    url(r'^cbv404/?$', TestCBVDecorator404.as_view(), name='cbv404'),
    url(r'^fbv/?$', 'userprofile.views.test_fbv_decorator', name='fbv'),
    url(r'^fbv404/?$', 'userprofile.views.test_fbv_decorator_404', name='fbv404'),
)
