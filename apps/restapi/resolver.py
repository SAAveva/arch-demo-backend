import functools

from django.conf import settings
from django.http import HttpResponseNotFound
from importlib import import_module

@functools.lru_cache(maxsize=None)
def resolver(request, *args, **kwargs):
    ''' bit hacky but works '''
    for app in settings.INSTALLED_APPS:
        try:
            module = import_module(app + '.views')
        except ImportError:
            pass

        for attr in dir(module):
            if attr.startswith('_'):
                continue
            
            call = getattr(module, attr)
            if callable(call) and hasattr(call, '__api_view'):
                print('reached here')
                if call.__api_url == request.path:# and request.method in call.__api_methods:
                    print(cal.__api_url,request.path)
                    return call(request, *args, **kwargs)

    return HttpResponseNotFound()


    
def api(url, methods=[]):
    def _api_add(call):
        @functools.wraps(call)
        def wrapped(request, *args, **kwargs):
           return call(request, *args, **kwargs)
        call.__api_url = url
        call.__api_methods = methods

        return wrapped

            return _api_add

api.__api_view = True

