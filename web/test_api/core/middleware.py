from django.http import HttpResponseForbidden


class CheckAPIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path.startswith('/api/test/') and not request.META.get('HTTP_API_KEY'):
            return HttpResponseForbidden('Access denied')
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response