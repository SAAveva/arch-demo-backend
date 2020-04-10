from django.http import HttpResponse, HttpResponseNotFound
import json
import functools

class Http500(Exception):
    pass

def api_view(methods=None):
    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if methods is None or args[0].method in methods:
                if args[0].method == 'POST':
                    args[0].POST = json.loads(args[0].body)

                response = HttpResponse(content_type='application/json')
                try:
                    response.write(json.dumps(func(*args, **kwargs)))
                except Http500 as err:
                    response.status_code = 500
                    response.write(err.args[0])
                    

                return response
            else:
                return HttpResponseNotFound(json.dumps({'error': '404 not found'}), content_type='application/json')

        return wrapped

    return wrapper
