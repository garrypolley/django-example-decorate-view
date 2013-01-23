# -*- coding: utf-8 -*-

from functools import wraps

from django.http import Http404


class Decorate404(object):

    "Name is needed so functools can wrap this decorator in later calls"
    __name__ = "Decorate404"

    def __init__(self, do_404=False):
        """
        The init is used so you can have simple decorator syntax and
        easily tell what is meant for use with this decorator vs what
        gets passed to the decorated function.
        """
        self.do_404 = do_404

    def __call__(self, view_function):

        # Wrap the view function so you return the proper function meta data
        @wraps(view_function)
        def decorated(request, *args, **kwargs):
            if self.do_404:
                raise Http404

            # Make sure you pass the request to the view function.
            # In a CBV this function is returned from:
            #    CBV.as_view()
            #
            # In a FBV the FBV is the function.
            return view_function(request, *args, **kwargs)

        # We return a function so that Django can call this "hidden/privte" function
        # with the desired request objects.  When wrapping a class based view or a
        # function based view you need to return a function that takes reqeust as
        # it's first parameter, so you can have consistant behavior.
        return decorated
