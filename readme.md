django-example-decorate-view
============================

A simple app to show decorating a CBV and a FBV in django using a class based decorator

See the comments in [userprofile/decorators.py](https://github.com/garrypolley/django-example-decorate-view/blob/master/userprofile/decorators.py) for more info.


### URLs

All the following urls use the same decorator.  Wanted to show parameter accepting class
based decorator being used for both FBVs and CBVs.

* /fbv  <-- function based view with decorator doing nothing
* /fbv404 <-- function based view with decorator forcing a 404

* /cbv  <-- class based view with decorator doing nothing
* /cbv404 <-- class based view with decorator forcing a 404
