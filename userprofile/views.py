# Create your views here.

from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .decorators import Decorate404


class TestCBVDecorator404(TemplateView):
    template_name = "dec_test.html"

    @method_decorator(Decorate404(do_404=True))
    def dispatch(self, *args, **kwargs):
        return super(TestCBVDecorator, self).dispatch(*args, **kwargs)


class TestCBVDecorator(TemplateView):
    template_name = "dec_test.html"

    @method_decorator(Decorate404())
    def dispatch(self, *args, **kwargs):
        return super(TestCBVDecorator, self).dispatch(*args, **kwargs)


@Decorate404(do_404=True)
def test_fbv_decorator_404(*args, **kwargs):
    return render_to_response('dec_test.html')


@Decorate404()
def test_fbv_decorator(*args, **kwargs):
    return render_to_response('dec_test.html')
