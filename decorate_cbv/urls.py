from django.conf.urls import patterns, url

from userprofile.views import TestCBVDecorator
from userprofile.views import TestCBVDecorator404
from userprofile.views import TestCBVFuncDecorator404
from userprofile.views import TestCBVFuncDecorator

urlpatterns = patterns('',
    # Examples:
    url(r'^cbv/?$', TestCBVDecorator.as_view(), name='cbv'),
    url(r'^cbv/func/?$', TestCBVFuncDecorator.as_view(), name='cbv404func'),
    url(r'^cbv404/?$', TestCBVDecorator404.as_view(), name='cbv404'),
    url(r'^cbv404/func/?$', TestCBVFuncDecorator404.as_view(), name='cbv404func'),
    url(r'^fbv/?$', 'userprofile.views.test_fbv_decorator', name='fbv'),
    url(r'^fbv/func/?$', 'userprofile.views.test_fbv_func_decorator', name='fbvfunc'),
    url(r'^fbv404/?$', 'userprofile.views.test_fbv_decorator_404', name='fbv404'),
    url(r'^fbv404/func/?$', 'userprofile.views.test_fbv_func_decorator404', name='fbv404func'),
)
